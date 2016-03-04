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

file_reactance = open('reflect_cap.csv', 'rb')  # open the file
reactance = csv.reader(file_reactance, delimiter=',')   # convert cvs file to python list

# extract information from csv and store in the following lists for plotting and processing
freq = []
reflect_cap = []

for row in reactance:   # row contains the row data
    if reactance.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(float(row[0]))  # frequency in GHz
        cap = 1/(-1*float(row[0])*float(row[1])) * 1000  # convert reactance to capacitance in pF
        reflect_cap.append(cap)

# poly fit reflect_cap data
z = np.polyfit(freq, reflect_cap, 3)  # use 3 degree poly
print z # higher order first

# turn poly coefficient into a function to compare
p = np.poly1d(z)
# print 'test polyfit equation1: %f' %p(freq[0])  # test
# print 'test polyfit equation2: %f' %p(freq[len(freq)-1])  # test

reflect_cap_polyfit = []
for i in range(0, len(freq)):
    reflect_cap_polyfit.append(p(freq[i]))    # create data set for comparison

plot.figure(1)
ax0 = plot.subplot(111)
ax0.plot(freq, reflect_cap, 'r-', label="simulated reflect_cap")
ax0.plot(freq, reflect_cap_polyfit, 'b-', label="poly-fit reflect_cap")
# ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('reflect standard capacitance (pF)')
plot.title('TRL reflect standard capacitance')
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.show()
