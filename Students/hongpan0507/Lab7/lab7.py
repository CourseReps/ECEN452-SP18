# Program Function:
#   1. plots the s21 measured_phase and magnitude from the measurement data (.csv) of a TRL line standard
#   2. poly curve fit the data and use the equation to extrapolate the data

# Notes:
#   1. poly fit example: http://stackoverflow.com/questions/19165259/python-numpy-scipy-curve-fitting
#   2. poly fit reference: http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.polyfit.html
#   3. p = np.poly1d(z) import poly fit result to create the poly equation, p(x) can be used as the poly equation

import csv
from matplotlib import pyplot as plot

file1 = open('Milled_Wilkinson_S11.csv', 'rb')  # open the file
meas_s11_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Wilkinson_S21.csv', 'rb')  # open the file
meas_s21_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Wilkinson_S22.csv', 'rb')  # open the file
meas_s22_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Wilkinson_S31.csv', 'rb')  # open the file
meas_s31_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Wilkinson_S32.csv', 'rb')  # open the file
meas_s32_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Wilkinson_S33.csv', 'rb')  # open the file
meas_s33_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list

file1 = open('lab7_wilkinson_s_para_mag.csv', 'rb')   # open the file
hfss_sim_s_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list

file1 = open('ECEN_452_Lab7_WPD_TL.csv', 'rb')   # open the file
z0lver_sim_s_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list

file2 = open('HP_LS_THRU.csv', 'rb')   # open the file
PS_0_deg1 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('HP_LS_THRU2.csv', 'rb')   # open the file
PS_0_deg2 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('HP_LS_90deg.csv', 'rb')   # open the file
PS_90_deg = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('HP_LS_180deg.csv', 'rb')   # open the file
PS_180_deg = csv.reader(file2, delimiter=',')   # convert cvs file to python list

# extract information from csv and store in the following lists for plotting and processing
freq = []
meas_s11_mag_data = []
meas_s22_mag_data = []
meas_s33_mag_data = []
meas_s21_mag_data = []
meas_s31_mag_data = []
meas_s32_mag_data = []

hfss_sim_s11_mag = []
hfss_sim_s22_mag = []
hfss_sim_s33_mag = []
hfss_sim_s21_mag = []
hfss_sim_s31_mag = []
hfss_sim_s32_mag = []

z0lver_sim_s11_mag = []
z0lver_sim_s22_mag = []
z0lver_sim_s33_mag = []
z0lver_sim_s21_mag = []
z0lver_sim_s31_mag = []
z0lver_sim_s32_mag = []

PS_0_deg_s11_mag1 = []
PS_0_deg_s21_mag1 = []
PS_0_deg_s11_phase1 = []
PS_0_deg_s21_phase1 = []

PS_0_deg_s11_mag2 = []
PS_0_deg_s21_mag2 = []
PS_0_deg_s11_phase2 = []
PS_0_deg_s21_phase2 = []

PS_90_deg_s11_mag = []
PS_90_deg_s21_mag = []
PS_90_deg_s11_phase = []
PS_90_deg_s21_phase = []

PS_180_deg_s11_mag = []
PS_180_deg_s21_mag = []
PS_180_deg_s11_phase = []
PS_180_deg_s21_phase = []

freq_marker = []
meas_s21_marker = []
hfss_sim_s21_marker = []
z0lver_sim_s21_marker = []
meas_s31_marker = []
hfss_sim_s31_marker = []
z0lver_sim_s31_marker = []
marker1 = 2.5

for row in meas_s11_mag:   # row contains the row data
    if meas_s11_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(float(row[0])/1e9)   # convert from Hz to GHz
        meas_s11_mag_data.append(float(row[1]))

for row in meas_s22_mag:   # row contains the row data
    if meas_s22_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        meas_s22_mag_data.append(float(row[1]))

for row in meas_s33_mag:   # row contains the row data
    if meas_s33_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        meas_s33_mag_data.append(float(row[1]))

for row in meas_s21_mag:   # row contains the row data
    if meas_s21_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        meas_s21_mag_data.append(float(row[1]))
        freq_num = float(row[0])/1e9
        if freq_num == marker1:
            freq_marker.append(freq_num)
            meas_s21_marker.append(float(row[1]))

for row in meas_s31_mag:   # row contains the row data
    if meas_s31_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        meas_s31_mag_data.append(float(row[1]))
        freq_num = float(row[0])/1e9
        if freq_num == marker1:
            meas_s31_marker.append(float(row[1]))

for row in meas_s32_mag:   # row contains the row data
    if meas_s32_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        meas_s32_mag_data.append(float(row[1]))

for row in hfss_sim_s_mag:   # row contains the row data
    if hfss_sim_s_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hfss_sim_s11_mag.append(float(row[1]))
        hfss_sim_s21_mag.append(float(row[2]))
        hfss_sim_s22_mag.append(float(row[3]))
        hfss_sim_s31_mag.append(float(row[4]))
        hfss_sim_s32_mag.append(float(row[5]))
        hfss_sim_s33_mag.append(float(row[6]))
        freq_num = float(row[0])
        if freq_num == marker1:
            hfss_sim_s21_marker.append(float(row[2]))
            hfss_sim_s31_marker.append(float(row[4]))

for row in z0lver_sim_s_mag:   # row contains the row data
    if z0lver_sim_s_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        z0lver_sim_s11_mag.append(float(row[1]))
        z0lver_sim_s21_mag.append(float(row[4]))
        z0lver_sim_s22_mag.append(float(row[5]))
        z0lver_sim_s31_mag.append(float(row[7]))
        z0lver_sim_s32_mag.append(float(row[8]))
        z0lver_sim_s33_mag.append(float(row[9]))
        freq_num = float(row[0])/1e9
        if freq_num == marker1:
            z0lver_sim_s21_marker.append(float(row[4]))
            z0lver_sim_s31_marker.append(float(row[7]))

for row in PS_0_deg1:   # row contains the row data
    if PS_0_deg1.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        PS_0_deg_s21_mag1.append(float(row[1]))
        PS_0_deg_s21_phase1.append(float(row[2]))
        PS_0_deg_s11_mag1.append(float(row[3]))
        PS_0_deg_s11_phase1.append(float(row[4]))

for row in PS_90_deg:   # row contains the row data
    if PS_90_deg.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        PS_90_deg_s21_mag.append(float(row[1]))
        PS_90_deg_s21_phase.append(float(row[2]))
        PS_90_deg_s11_mag.append(float(row[3]))
        PS_90_deg_s11_phase.append(float(row[4]))

for row in PS_180_deg:   # row contains the row data
    if PS_180_deg.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        PS_180_deg_s21_mag.append(float(row[1]))
        PS_180_deg_s21_phase.append(float(row[2]))
        PS_180_deg_s11_mag.append(float(row[3]))
        PS_180_deg_s11_phase.append(float(row[4]))

n = 0
# n += 1
# plot.figure(n)
# ax0 = plot.subplot(111)
# ax0.plot(freq, meas_s11_mag_data, 'r-', label="measured |s11|")
# ax0.plot(freq, hfss_sim_s11_mag, 'b-', label="hfss simulated |s11|")
# ax0.plot(freq, z0lver_sim_s11_mag, 'g-', label="z0lver simulated |s11|")
# ax0.axis([1, 5, -60, 0])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (GHz)')
# plot.ylabel('|s11| (dB)')
# plot.title('Wilkinson Power Divider')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
#
# n += 1
# plot.figure(n)
# ax0 = plot.subplot(111)
# ax0.plot(freq, meas_s22_mag_data, 'r-', label="measured |s22|")
# ax0.plot(freq, hfss_sim_s22_mag, 'b-', label="hfss simulated |s22|")
# ax0.plot(freq, z0lver_sim_s22_mag, 'g-', label="z0lver simulated |s22|")
# ax0.axis([1, 5, -60, 0])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (GHz)')
# plot.ylabel('|s22| (dB)')
# plot.title('Wilkinson Power Divider')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
#
# n += 1
# plot.figure(n)
# ax0 = plot.subplot(111)
# ax0.plot(freq, meas_s33_mag_data, 'r-', label="measured |s33|")
# ax0.plot(freq, hfss_sim_s33_mag, 'b-', label="hfss simulated |s33|")
# ax0.plot(freq, z0lver_sim_s33_mag, 'g-', label="z0lver simulated |s33|")
# ax0.axis([1, 5, -60, 0])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (GHz)')
# plot.ylabel('|s33| (dB)')
# plot.title('Wilkinson Power Divider')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
#
# n += 1
# plot.figure(n)
# ax0 = plot.subplot(111)
# ax0.plot(freq, meas_s21_mag_data, 'r-', label="measured |s21|")
# ax0.plot(freq, hfss_sim_s21_mag, 'b-', label="hfss simulated |s21|")
# ax0.plot(freq, z0lver_sim_s21_mag, 'g-', label="z0lver simulated |s21|")
# ax0.scatter(freq_marker, meas_s21_marker, s=80, marker="o", color='r', label=("x="+str(freq_marker)+"\ny="+str(meas_s21_marker)))
# ax0.scatter(freq_marker, hfss_sim_s21_marker, s=80, marker="o", color='b', label=("x="+str(freq_marker)+"\ny="+str(hfss_sim_s21_marker)))
# # ax0.scatter(freq_marker, z0lver_sim_s21_marker, s=80, marker="+", color='g', label=("x="+str(freq_marker)+"\ny="+str(z0lver_sim_s21_marker)))
# ax0.axis([1, 5, -10, 0])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (GHz)')
# plot.ylabel('|s21| (dB)')
# plot.title('Wilkinson Power Divider')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
#
# n += 1
# plot.figure(n)
# ax0 = plot.subplot(111)
# ax0.plot(freq, meas_s31_mag_data, 'r-', label="measured |s31|")
# ax0.plot(freq, hfss_sim_s31_mag, 'b-', label="hfss simulated |s31|")
# ax0.plot(freq, z0lver_sim_s31_mag, 'g-', label="z0lver simulated |s31|")
# ax0.scatter(freq_marker, meas_s31_marker, s=80, marker="o", color='r', label=("x="+str(freq_marker)+"\ny="+str(meas_s31_marker)))
# ax0.scatter(freq_marker, hfss_sim_s31_marker, s=80, marker="o", color='b', label=("x="+str(freq_marker)+"\ny="+str(hfss_sim_s31_marker)))
# # ax0.scatter(freq_marker, z0lver_sim_s31_marker, s=80, marker="+", color='g', label=("x="+str(freq_marker)+"\ny="+str(z0lver_sim_s31_marker)))
# ax0.axis([1, 5, -10, 0])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (GHz)')
# plot.ylabel('|s31| (dB)')
# plot.title('Wilkinson Power Divider')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
#
# n += 1
# plot.figure(n)
# ax0 = plot.subplot(111)
# ax0.plot(freq, meas_s32_mag_data, 'r-', label="measured |s32|")
# ax0.plot(freq, hfss_sim_s32_mag, 'b-', label="hfss simulated |s32|")
# ax0.plot(freq, z0lver_sim_s32_mag, 'g-', label="z0lver simulated |s32|")
# ax0.axis([1, 5, -60, 0])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (GHz)')
# plot.ylabel('|s32| (dB)')
# plot.title('Wilkinson Power Divider')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, PS_0_deg_s11_mag1, 'r-', label="0deg; measured |s11|")
ax0.plot(freq, PS_90_deg_s11_mag, 'b-', label="90deg; measured |s11|")
ax0.plot(freq, PS_180_deg_s11_mag, 'g-', label="180deg; measured |s11|")
ax0.axis([1, 5, -50, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('Phase Shifter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, PS_0_deg_s21_mag1, 'r-', label="0deg; measured |s21|")
ax0.plot(freq, PS_90_deg_s21_mag, 'b-', label="90deg; measured |s21|")
ax0.plot(freq, PS_180_deg_s21_mag, 'g-', label="180deg; measured |s21|")
ax0.axis([1, 5, -10, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('Phase Shifter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, PS_0_deg_s11_phase1, 'r-', label="0deg; measured s11 phase")
ax0.plot(freq, PS_90_deg_s11_phase, 'b-', label="90deg; measured s11 phase")
ax0.plot(freq, PS_180_deg_s11_phase, 'g-', label="180deg; measured s11 phase")
# ax0.axis([1, 5, -10, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('phase (deg)')
plot.title('Phase Shifter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, PS_0_deg_s21_phase1, 'r-', label="0deg; measured s21 phase")
ax0.plot(freq, PS_90_deg_s21_phase, 'b-', label="90deg; measured s21 phase")
ax0.plot(freq, PS_180_deg_s21_phase, 'g-', label="180deg; measured s21 phase")
# ax0.axis([1, 5, -10, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('phase (deg)')
plot.title('Phase Shifter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

plot.show()

file1.close()
