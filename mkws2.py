import cantera as ct
from sdtoolbox.postshock import CJspeed
from sdtoolbox.postshock import PostShock_eq
from sdtoolbox.thermo import soundspeed_eq, soundspeed_fr
import numpy as np
import matplotlib.pyplot as plt
from sdtoolbox.utilities import CJspeed_plot, znd_plot
from sdtoolbox.postshock import CJspeed, PostShock_fr, PostShock_eq
from sdtoolbox.znd import zndsolve
from sdtoolbox.cv import cvsolve
from sdtoolbox.utilities import CJspeed_plot, znd_plot
from matplotlib import pyplot as plt

P0 = 101325.0
T0 = 293

npoints = 20


q2 = 'CH4:1 O2:1 N2:3.76'
q3 = 'C2H6:0.5714 O2:1 N2:3.76'
q4 = 'C3H8:0.4 O2:1 N2:3.76'


mech = 'gri30.xml'

gas_initial2 = ct.Solution(mech)
gas_initial2.TPX = T0, P0, q2

gas_initial3 = ct.Solution(mech)
gas_initial3.TPX = T0, P0, q3

gas_initial4 = ct.Solution(mech)
gas_initial4.TPX = T0, P0, q4

# compute CJ speed fo different prssures

speed2 = np.zeros(npoints)
speed3 = np.zeros(npoints)
speed4 = np.zeros(npoints)

P = np.linspace(0.1*ct.one_atm, ct.one_atm*3, npoints)


for i in range(npoints):
    
    
    
    [cj_speed,R2,plot_data] = CJspeed(P[i], T0, q2, mech, fullOutput=True)  
    speed2[i] = cj_speed
    
    [cj_speed,R2,plot_data] = CJspeed(P[i], T0, q3, mech, fullOutput=True)  
    speed3[i] = cj_speed
    
    [cj_speed,R2,plot_data] = CJspeed(P[i], T0, q4, mech, fullOutput=True)  
    speed4[i] = cj_speed



fig, ax = plt.subplots(figsize=(12,8))
ax.plot(P/100000, speed2, label = 'CH4')
ax.plot(P/100000, speed3, label = 'C2H6')
ax.plot(P/100000, speed4, label = 'C3H8')
ax.set(xlabel='Pressure [bar]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.title("")
plt.legend()
fig.savefig('pvar.png', dpi=100)
plt.show()



npoints2 = 20

T = np.linspace(273, 2000, npoints2)

speed5 = np.zeros(npoints2)
speed6 = np.zeros(npoints2)
speed7 = np.zeros(npoints2)

for i in range(npoints2):
    
    [cj_speed,R2,plot_data] = CJspeed(P0, T[i], q2, mech, fullOutput=True)  
    speed5[i] = cj_speed

    [cj_speed,R2,plot_data] = CJspeed(P0, T[i], q3, mech, fullOutput=True)  
    speed6[i] = cj_speed
    
    [cj_speed,R2,plot_data] = CJspeed(P0, T[i], q4, mech, fullOutput=True)  
    speed7[i] = cj_speed


fig, ax = plt.subplots(figsize=(12,8))
ax.plot(T, speed5, label = 'CH4')
ax.plot(T, speed6, label = 'C2H6')
ax.plot(T, speed7, label = 'C3H8')
ax.set(xlabel='Temperature [K]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.title("")
plt.legend()
fig.savefig('Tvar.png', dpi=100)
plt.show()






