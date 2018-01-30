from cmath import pi, atan
import numpy as np
from matplotlib import pyplot as plot

freq = 2.45e9
w = 2 * pi * freq

c_min = 0.5e-12
c_max = 10e-12
c_step = 0.1e-12
c = np.arange(c_min, c_max, c_step)     # varactor range

z0 = 50
z_T1 = np.arange(20, 80, 10)    # plot with different z_T1

rad_to_ang = 180 / pi

gamma_ang = []
for j in range(0, len(z_T1)):
    temp = []
    for i in range(0, len(c)):
        zL = -1j / (w * c[i])  # convert to impedance
        z_in = z_T1[j]**2 / zL     # quarter wave transformer
        gamma = (z_in - z0)/(z_in + z0)
        temp.append(np.angle(gamma)*rad_to_ang)
    gamma_ang.append(temp)

plot.figure(1, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
for i in range(0, len(z_T1)):
    plot.plot(c, gamma_ang[i], label= "z_T1 = " + str(z_T1[i]))

plot.ylabel('angle(deg)')
plot.xlabel('C (pF)')
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

plot.show()
