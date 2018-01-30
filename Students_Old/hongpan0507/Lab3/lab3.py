# Program Function:
#   1. plots the s21 phase and magnitude from the measurement data (.csv) of a TRL line standard
#   2. poly curve fit the data and use the equation to extrapolate the data

# Notes:
#   1. poly fit example: http://stackoverflow.com/questions/19165259/python-numpy-scipy-curve-fitting
#   2. poly fit reference: http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.polyfit.html
#   3. p = np.poly1d(z) import poly fit result to create the poly equation, p(x) can be used as the poly equation

import csv
from matplotlib import pyplot as plot
import numpy as np

file_phase = open('TRL_Demo_Line_S21_Phase.csv', 'rb')  # open the file
file_mag = open('TRL_Demo_Line_S21_dB.csv', 'rb')   # open the file
s21_phase = csv.reader(file_phase, delimiter=',')   # convert cvs file to python list
s21_mag = csv.reader(file_mag, delimiter=',')   # convert cvs file to python list

# extract information from csv and store in the following lists for plotting and processing
freq = []
phase = []
mag = []

for row in s21_phase:   # row contains the row data
    if s21_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(float(row[0])/1e9)   # convert from Hz to GHz
        phase.append(float(row[1]))

for row in s21_mag:   # row contains the row data
    if s21_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        mag.append(float(row[1]))

# poly fit phase data
z = np.polyfit(freq, phase, 1)  # use 1 degree poly

# turn poly coefficient into a function to compare
p = np.poly1d(z)
print 'test polyfit equation1: %f' %p(freq[0])  # test
print 'test polyfit equation2: %f' %p(freq[len(freq)-1])  # test

phase_polyfit = []
for i in range(0, len(freq)):
    phase_polyfit.append(p(freq[i]))    # create data set for comparison

# extrapolate the frequency when phase = 20 deg and 160 deg
freq_L = (-20 - z[1])/z[0]
freq_H = (-160 - z[1])/z[0]
print 'Lower frequency = %f' % freq_L
print 'Upper frequency = %f' % freq_H

plot.figure(1)
ax0 = plot.subplot(211)
ax0.plot(freq, phase, 'r-', label="measured s21 phase")
ax0.plot(freq, phase_polyfit, 'b-', label="poly-fit s21 phase")
ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('S21 Phase (deg)')
plot.title('TRL Line S21 Phase')
plot.legend(loc=4)  # loc=4 => bottom right corner

ax1 = plot.subplot(212)
ax1.plot(freq, mag, 'r-', label="s21 mag")
ax1.axis([1.5, 4.5, -0.25, 0.25])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('S21 magnitude (dB)')
plot.title('TRL Line S21 Magnitude')
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.show()
