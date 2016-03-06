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
file1 = open('sim_TRL_reflect_s11_mag.csv', 'rb')  # open the file for reading
sim_csv_reflect_s11_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('sim_TRL_thru_s11_s21_mag.csv', 'rb')  # open the file for reading
sim_csv_thru_s11_s21_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('sim_TRL_thru_s21_phase.csv', 'rb')  # open the file for reading
sim_csv_thru_s21_phase = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('sim_TRL_line_s11_s21_mag.csv', 'rb')  # open the file for reading
sim_csv_line_s11_s21_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('sim_TRL_line_s21_phase.csv', 'rb')  # open the file for reading
sim_csv_line_s21_phase = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('S21_Thru_dB.csv', 'rb')  # open the file for reading
measured_csv_thru_s21_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('S21_Thru_Phase.csv', 'rb')  # open the file for reading
measured_csv_thru_s21_phase = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('S21_Line_dB.csv', 'rb')  # open the file for reading
measured_csv_line_s21_mag = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('S21_Line_Phase.csv', 'rb')  # open the file for reading
measured_csv_line_s21_phase = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []
sim_reflect_s11_mag = []
sim_thru_s11_mag = []
sim_thru_s21_mag = []
sim_thru_s21_phase = []
sim_line_s11_mag = []
sim_line_s21_mag = []
sim_line_s21_phase = []

measured_thru_s21_mag = []
measured_thru_s21_phase = []
measured_line_s21_mag = []
measured_line_s21_phase = []

# ***************************** Simulated Data *****************************
for row in sim_csv_reflect_s11_mag:   # row contains the row data
    if sim_csv_reflect_s11_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])     # frequency in GHz
        sim_reflect_s11_mag.append(row[1])     # s11 mag

for row in sim_csv_thru_s11_s21_mag:   # row contains the row data
    if sim_csv_thru_s11_s21_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_thru_s11_mag.append(row[1])     # s11 mag
        sim_thru_s21_mag.append(row[2])     # s21 mag

for row in sim_csv_thru_s21_phase:
    if sim_csv_thru_s21_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_thru_s21_phase.append(row[1])     # s21 phase

for row in sim_csv_line_s11_s21_mag:   # row contains the row data
    if sim_csv_line_s11_s21_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_line_s11_mag.append(row[1])     # s11 mag
        sim_line_s21_mag.append(row[2])     # s21 mag

for row in sim_csv_line_s21_phase:
    if sim_csv_line_s21_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_line_s21_phase.append(row[1])     # s21 phase
# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_thru_s21_mag:   # row contains the row data
    if measured_csv_thru_s21_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_thru_s21_mag.append(row[1])     # s21 mag


for row in measured_csv_thru_s21_phase:   # row contains the row data
    if measured_csv_thru_s21_phase.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_thru_s21_phase.append(row[1])     # s21 phase

for row in measured_csv_line_s21_mag:   # row contains the row data
    if measured_csv_line_s21_mag.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_line_s21_mag.append(row[1])     # s21 mag

for row in measured_csv_line_s21_phase:   # row contains the row data
    if measured_csv_line_s21_phase.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_line_s21_phase.append(row[1])     # s21 phase
# *************************************************************************

plot.figure(1)
ax0 = plot.subplot(111)
ax0.plot(freq, sim_reflect_s11_mag, 'r-', label="simulated reflect |s11|")
ax0.axis([1, 5, -0.5, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Reflect standard |S11| (dB) ')
plot.title('TRL reflect standard S11 magnitude')
plot.legend(loc=4)  # loc=4 => bottom right corner

plot.figure(2)
ax0 = plot.subplot(111)
ax0.plot(freq, sim_thru_s11_mag, 'r-', label="simulated thru |s11|")
ax0.axis([1, 5, -60, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Thru standard |S11| (dB) ')
plot.title('TRL thru standard S11 magnitude')
plot.legend(loc=1)  # loc=4 => bottom right corner

plot.figure(3)
ax0 = plot.subplot(211)
ax0.plot(freq, sim_thru_s21_mag, 'r-', label="simulated thru |s21|")
ax0.plot(freq, measured_thru_s21_mag, 'b-', label="measured thru |s21|")
ax0.axis([1, 5, -1, 1])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Thru standard |S21| (dB) ')
plot.title('TRL thru standard S21 magnitude')
plot.legend(loc=4)  # loc=4 => bottom right corner
ax0 = plot.subplot(212)
ax0.plot(freq, sim_thru_s21_phase, 'r-', label="simulated thru s21 phase")
ax0.plot(freq, measured_thru_s21_phase, 'b-', label="measured thru s21 phase")
ax0.axis([1, 5, -5, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Thru standard S21 (deg) ')
plot.title('TRL thru standard S21 phase')
plot.legend(loc=1)  # loc=4 => bottom right corner

plot.figure(4)
ax0 = plot.subplot(111)
ax0.plot(freq, sim_line_s11_mag, 'r-', label="simulated line |s11|")
ax0.axis([1, 5, -60, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Line standard |S11| (dB) ')
plot.title('TRL line standard S11 magnitude')
plot.legend(loc=1)  # loc=4 => bottom right corner

plot.figure(5)
ax0 = plot.subplot(211)
ax0.plot(freq, sim_line_s21_mag, 'r-', label="simulated line |s21|")
ax0.plot(freq, measured_line_s21_mag, 'b-', label="measured line |s21|")
ax0.axis([1, 5, -3, 1])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('line standard |S21| (dB) ')
plot.title('TRL line standard S21 magnitude')
plot.legend(loc=4)  # loc=4 => bottom right corner
ax0 = plot.subplot(212)
ax0.plot(freq, sim_line_s21_phase, 'r-', label="simulated line s21 phase")
ax0.plot(freq, measured_line_s21_phase, 'b-', label="measured line s21 phase")
ax0.axis([1, 5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Line standard S21 (deg) ')
plot.title('TRL line standard S21 phase')
plot.legend(loc=1)  # loc=4 => bottom right corner

plot.show()

file1.close()
file2.close()
