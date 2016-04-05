# Program Function:
#   1. plots the s21 measured_phase and magnitude from the measurement data (.csv) of a TRL line standard
#   2. poly curve fit the data and use the equation to extrapolate the data

# Notes:
#   1. poly fit example: http://stackoverflow.com/questions/19165259/python-numpy-scipy-curve-fitting
#   2. poly fit reference: http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.polyfit.html
#   3. p = np.poly1d(z) import poly fit result to create the poly equation, p(x) can be used as the poly equation

import csv
from matplotlib import pyplot as plot

file1 = open('HP_JP_BSF_dB.csv', 'rb')  # open the file
measured_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('HP_JP_BSF_phase.csv', 'rb')   # open the file
measured_phase = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file2 = open('lab6_BSF_s_para_mag.csv', 'rb')  # open the file
sim_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('lab6_BSF_s_para_phase.csv', 'rb')  # open the file
sim_phase = csv.reader(file2, delimiter=',')   # convert cvs file to python list

file3 = open('Milled_LPF_dB.csv', 'rb')  # open the file
LPF_meas_mag = csv.reader(file3, delimiter=',')   # convert cvs file to python list
file3 = open('Milled_LPF_phase.csv', 'rb')  # open the file
LPF_meas_phase = csv.reader(file3, delimiter=',')   # convert cvs file to python list
file3 = open('lab6_LPF_s_para_mag.csv', 'rb')  # open the file
LPF_hfss_mag = csv.reader(file3, delimiter=',')   # convert cvs file to python list
file3 = open('lab6_LPF_s_para_phase.csv', 'rb')  # open the file
LPF_hfss_phase = csv.reader(file3, delimiter=',')   # convert cvs file to python list

# extract information from csv and store in the following lists for plotting and processing
freq = []
measured_s11_phase = []
measured_s11_mag = []
measured_s21_phase = []
measured_s21_mag = []
sim_s11_phase = []
sim_s11_mag = []
sim_s21_phase = []
sim_s21_mag = []

LPF_meas_s11_phase = []
LPF_meas_s11_mag = []
LPF_meas_s21_phase = []
LPF_meas_s21_mag = []
LPF_hfss_s11_phase = []
LPF_hfss_s11_mag = []
LPF_hfss_s21_phase = []
LPF_hfss_s21_mag = []

for row in measured_phase:   # row contains the row data
    if measured_phase.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(float(row[0])/1e9)   # convert from Hz to GHz
        measured_s11_phase.append(float(row[1]))
        measured_s21_phase.append(float(row[2]))

for row in measured_mag:   # row contains the row data
    if measured_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag.append(float(row[1]))
        measured_s21_mag.append(float(row[2]))

for row in sim_phase:   # row contains the row data
    if sim_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_s11_phase.append(float(row[1]))
        sim_s21_phase.append(float(row[2]))

for row in sim_mag:   # row contains the row data
    if sim_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_s11_mag.append(float(row[1]))
        sim_s21_mag.append(float(row[2]))

for row in LPF_meas_phase:   # row contains the row data
    if LPF_meas_phase.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        LPF_meas_s11_phase.append(float(row[1]))
        LPF_meas_s21_phase.append(float(row[2]))

for row in LPF_meas_mag:   # row contains the row data
    if LPF_meas_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        LPF_meas_s11_mag.append(float(row[1]))
        LPF_meas_s21_mag.append(float(row[2]))

for row in LPF_hfss_phase:   # row contains the row data
    if LPF_hfss_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        LPF_hfss_s11_phase.append(float(row[1]))
        LPF_hfss_s21_phase.append(float(row[2]))

for row in LPF_hfss_mag:   # row contains the row data
    if LPF_hfss_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        LPF_hfss_s11_mag.append(float(row[1]))
        LPF_hfss_s21_mag.append(float(row[2]))

n = 0
n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, measured_s21_phase, 'r-', label="s21 measured_phase")
ax0.plot(freq, sim_s21_phase, 'b-', label="s21 simulated_phase")
# ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('phase (deg)')
plot.title('5th order Band Stop Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax1 = plot.subplot(111)
ax1.plot(freq, measured_s21_mag, 'r-', label="s21 measured_mag")
ax1.plot(freq, sim_s21_mag, 'b-', label="s21 simulated_mag")
# ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('magnitude (dB)')
plot.title('5th order Band Stop Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, measured_s11_phase, 'r-', label="s11 measured_phase")
ax0.plot(freq, sim_s11_phase, 'b-', label="s11 simulated_phase")
# ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('phase (deg)')
plot.title('5th order Band Stop Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax1 = plot.subplot(111)
ax1.plot(freq, measured_s11_mag, 'r-', label="s11 measured_mag")
ax1.plot(freq, sim_s11_mag, 'b-', label="s11 simulated_mag")
# ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('magnitude (dB)')
plot.title('5th order Band Stop Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax1 = plot.subplot(111)
ax1.plot(freq, LPF_meas_s11_mag, 'r-', label="measured s11 mag")
ax1.plot(freq, LPF_hfss_s11_mag, 'b-', label="hfss s11 mag")
# ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('magnitude (dB)')
plot.title('5th order Low Pass Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax1 = plot.subplot(111)
ax1.plot(freq, LPF_meas_s21_mag, 'r-', label="measured s21 mag")
ax1.plot(freq, LPF_hfss_s21_mag, 'b-', label="hfss s21 mag")
# ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('magnitude (dB)')
plot.title('5th order Low Pass Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax1 = plot.subplot(111)
ax1.plot(freq, LPF_meas_s11_phase, 'r-', label="measured s11 phase")
ax1.plot(freq, LPF_hfss_s11_phase, 'b-', label="hfss s11 phase")
# ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('phase (deg)')
plot.title('5th order Low Pass Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax1 = plot.subplot(111)
ax1.plot(freq, LPF_meas_s21_phase, 'r-', label="measured s21 phase")
ax1.plot(freq, LPF_hfss_s21_phase, 'b-', label="hfss s21 phase")
# ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('phase (deg)')
plot.title('5th order Low Pass Filter')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

plot.show()

file1.close()
