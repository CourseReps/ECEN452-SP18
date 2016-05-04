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

# -----------------------first section only--------------------------
gamma_ang1 = []
for j in range(0, len(z_T1)):
    temp = []
    for i in range(0, len(c)):
        zL1 = -1j / (w * c[i])  # convert to impedance
        z_in1 = z_T1[j]**2 / zL1     # quarter wave transformer
        gamma = (z_in1 - z0)/(z_in1 + z0)
        temp.append(np.angle(gamma)*rad_to_ang)
    gamma_ang1.append(temp)

# -----------------------two sections--------------------------
gamma_ang2 = []   # data format = [ration_T1_T2[z_T1[]]]
ratio_T1_T2 = np.arange(0.2, 1, 0.2)
for i in range(0, len(ratio_T1_T2)):
    temp0 = []
    for k in range(0, len(z_T1)):
        temp1 = []
        for j in range(0, len(c)):
            x = -1/(w * c[j])
            z_in1 = 1j*(ratio_T1_T2[i]**2*x - z_T1[k]/x)
            gamma = (z_in1 - z0)/(z_in1 + z0)
            temp1.append(np.angle(gamma)*rad_to_ang)
        temp0.append(temp1)
    gamma_ang2.append(temp0)

for j in range(0, len(ratio_T1_T2)):
    plot.figure(j, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
    for i in range(0, len(z_T1)):
        plot.plot(c, gamma_ang1[i], '-', label="z_T1 = " + str(z_T1[i]))
        plot.plot(c, gamma_ang2[j][i], '--', label="z_T1 = " + str(z_T1[i]) + "; z_T1/z_T2 = " + str(ratio_T1_T2[j]))
    plot.ylabel('angle(deg)')
    plot.xlabel('C (pF)')
    plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
    plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

plot.show()
