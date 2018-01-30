from cmath import pi, atan
import numpy as np
from matplotlib import pyplot as plot

freq = 2.45e9
w = 2 * pi * freq

c_min = 0.7e-12
c_max = 8.8e-12
c_step = 0.1e-12
c = np.arange(c_min, c_max, c_step)     # varactor range

z0 = 50
z_T1 = np.arange(20, 80, 10)    # plot with different z_T1
ratio_T1_T2 = np.arange(0.8, 1.6, 0.2)

rad_to_ang = 180 / pi

# -----------------------first section only--------------------------
gamma_ang1 = []
for j in range(0, len(z_T1)):
    temp = []
    for i in range(0, len(c)):
        zL1 = -1j / (w * c[i])  # convert to impedance
        z_in1 = z_T1[j]**2 / zL1     # quarter wave transformer
        gamma = (z_in1 - z0)/(z_in1 + z0)
        temp.append(np.angle(gamma))
    gamma_ang1.append(np.unwrap(temp)*rad_to_ang)

# -----------------------two sections without inductor--------------------------
gamma_ang2 = []   # data format = [ration_T1_T2[z_T1[]]]
# ratio_T1_T2_1 = np.arange(0.2, 1, 0.2)
# ratio_T1_T2_2 = np.arange(1, 5, 1)
# ratio_T1_T2 = np.append(ratio_T1_T2_1, ratio_T1_T2_2)

for i in range(0, len(ratio_T1_T2)):
    temp0 = []
    for k in range(0, len(z_T1)):
        temp1 = []
        for j in range(0, len(c)):
            z_T2 = z_T1[k]/ratio_T1_T2[i]
            z_c = 1/(1j*w * c[j])   # capacitor
            z_in2 = z_T2**2 / z_c   # quarter wave transformer
            z_parallel = (1/z_c + 1/z_in2)**-1
            z_in1 = z_T1[k]**2/z_parallel
            gamma = (z_in1 - z0)/(z_in1 + z0)
            temp1.append(np.angle(gamma))   # in radian
        temp0.append(temp1)
    gamma_ang2.append(np.unwrap(temp0)*rad_to_ang)

# -----------------------two sections with inductor--------------------------
gamma_ang3 = []   # data format = [ration_T1_T2[z_T1[]]]

L = 3.4e-9  # inductance

for i in range(0, len(ratio_T1_T2)):
    temp0 = []
    for k in range(0, len(z_T1)):
        temp1 = []
        for j in range(0, len(c)):
            z_T2 = z_T1[k]/ratio_T1_T2[i]
            z_c = 1/(1j*w * c[j])   # capacitor
            z_i = 1j*w * L   # inductor
            z_L = z_c + z_i     # capacitor and inductor in series
            z_in2 = z_T2**2 / z_L
            z_parallel = (1/z_L + 1/z_in2)**-1
            z_in1 = z_T1[k]**2/z_parallel
            gamma = (z_in1 - z0)/(z_in1 + z0)
            temp1.append(np.angle(gamma))   # in radian
        temp0.append(temp1)
    gamma_ang3.append(np.unwrap(temp0)*rad_to_ang)

# -----------------------two sections with inductor and complete varactor model--------------------------
gamma_ang4 = []   # data format = [ration_T1_T2[z_T1[]]]

L = 3.4e-9  # inductor
z_i = 1j*w * L
R_s = 4.9   # varactor loss
C_p = 0.54e-16  # parasitic capacitance
z_p = 1/(1j*w*C_p)
L_s = 0.7e-9    # lead inductance
z_s = 1j*w*L_s

for i in range(0, len(ratio_T1_T2)):
    temp0 = []
    for k in range(0, len(z_T1)):
        temp1 = []
        for j in range(0, len(c)):
            z_T2 = z_T1[k]/ratio_T1_T2[i]
            z_c = 1/(1j*w * c[j])   # capacitor
            z_temp = R_s + z_c  # in series with R_s
            z_temp = (1/z_temp + 1/z_p)**-1     # in parallel with C_p
            z_L = z_s + z_temp + z_i    # all three in series
            z_in2 = z_T2**2 / z_L   # quarter wave transformer
            z_parallel = (1/z_L + 1/z_in2)**-1  # in parallel
            z_in1 = z_T1[k]**2/z_parallel   # quarter wave transformer
            gamma = (z_in1 - z0)/(z_in1 + z0)
            temp1.append(np.angle(gamma))   # in radian
        temp0.append(temp1)
    gamma_ang4.append(np.unwrap(temp0)*rad_to_ang)

for j in range(0, len(ratio_T1_T2)):
    plot.figure(j, figsize=(18, 10), dpi=80, facecolor='w', edgecolor='k')
    for i in range(0, len(z_T1)):
        plot.plot(c, gamma_ang1[i], '-', label="z_T1 = " + str(z_T1[i]))
        plot.plot(c, gamma_ang2[j][i], '--', label="z_T1 = " + str(z_T1[i]) + "; z_T1/z_T2 = " + str(ratio_T1_T2[j]) + "; z_T2 = " + str(z_T1[i]/ratio_T1_T2[j]))
        plot.plot(c, gamma_ang3[j][i], '+', label="z_T1 = " + str(z_T1[i]) + "; z_T1/z_T2 = " + str(ratio_T1_T2[j]) + "; z_T2 = " + str(z_T1[i]/ratio_T1_T2[j]))
        plot.plot(c, gamma_ang4[j][i], 'x', label="z_T1 = " + str(z_T1[i]) + "; z_T1/z_T2 = " + str(ratio_T1_T2[j]) + "; z_T2 = " + str(z_T1[i]/ratio_T1_T2[j]))
    plot.axis([0.5e-12, 10e-12, -800, 200])     # [xmin, xmax, ymin, ymax]
    plot.ylabel('angle(deg)')
    plot.xlabel('C (pF)')
    plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
    plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

plot.show()
