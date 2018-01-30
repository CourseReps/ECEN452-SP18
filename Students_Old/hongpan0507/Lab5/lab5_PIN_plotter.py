# Program Function:
#   plots the capacitance from the simulation data (.csv) of a TRL reflect standard
#   3 degree poly curve fit the data and output the coefficients
#   plots the curve based on poly equation and overlay to the simulation data
#   Calculate the delay required by the VNA

# Notes:
#   poly fit example: http://stackoverflow.com/questions/19165259/python-numpy-scipy-curve-fitting
#   poly fit reference: http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.polyfit.html
#   p = np.poly1d(z) import poly fit result to create the poly equation, p(x) can be used as the poly equation

import csv
from matplotlib import pyplot as plot
import numpy as np

# ***************************** Simulated Data *****************************
file1 = open('PIN_s11_s21_mag.csv', 'rb')  # open the file for reading
sim_csv_s11_s21_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('S11_OFF_dB.csv', 'rb')  # open the file for reading
measured_csv_s11_off_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('S11_ON_dB.csv', 'rb')  # open the file for reading
measured_csv_s11_on_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('S21_OFF_dB.csv', 'rb')  # open the file for reading
measured_csv_s21_off_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('S21_ON_dB.csv', 'rb')  # open the file for reading
measured_csv_s21_on_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []
sim_s11_mag_on = []
sim_s11_mag_off = []
sim_s21_mag_on = []
sim_s21_mag_off = []

measured_s11_mag_on = []
measured_s11_mag_off = []
measured_s21_mag_on = []
measured_s21_mag_off = []

# ***************************** Simulated Data *****************************
for row in sim_csv_s11_s21_mag:   # row contains the row data
    if sim_csv_s11_s21_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])     # frequency in GHz
        sim_s11_mag_off.append(row[1])     # s11 mag; off
        sim_s11_mag_on.append(row[2])     # s11 mag; on
        sim_s21_mag_off.append(row[3])     # s21 mag; off
        sim_s21_mag_on.append(row[4])     # s21 mag; on

# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_s11_on_mag:   # row contains the row data
    if measured_csv_s11_on_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_on.append(row[1])

for row in measured_csv_s11_off_mag:   # row contains the row data
    if measured_csv_s11_off_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_off.append(row[1])

for row in measured_csv_s21_on_mag:   # row contains the row data
    if measured_csv_s21_on_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s21_mag_on.append(row[1])

for row in measured_csv_s21_off_mag:   # row contains the row data
    if measured_csv_s21_off_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s21_mag_off.append(row[1])
# *************************************************************************

plot.figure(1)
ax0 = plot.subplot(211)
ax0.plot(freq, sim_s11_mag_on, 'r-', label="simulated |s11|; on state")
ax0.plot(freq, sim_s11_mag_off, 'b-', label="simulated |s11|; off state")
ax0.plot(freq, measured_s11_mag_on, 'r--', label="measured |s11|; on state")
ax0.plot(freq, measured_s11_mag_off, 'b--', label="measured |s11|; off state")
ax0.axis([1, 5, -30, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('PIN Diode |S11| (dB)')
plot.title('PIN Diode |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

ax0 = plot.subplot(212)
ax0.plot(freq, sim_s21_mag_on, 'r-', label="simulated |s21|; on state")
ax0.plot(freq, sim_s21_mag_off, 'b-', label="simulated |s21|; off state")
ax0.plot(freq, measured_s21_mag_on, 'r--', label="measured |s21|; on state")
ax0.plot(freq, measured_s21_mag_off, 'b--', label="measured |s21|; off state")
ax0.axis([1, 5, -30, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('PIN Diode |S21| (dB)')
plot.title('PIN Diode |S21|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

plot.show()

file1.close()
file2.close()
