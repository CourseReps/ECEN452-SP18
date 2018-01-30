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

freq_c = 3e9    # center frequency
DeEmbed_l = 15e-3      # de-embed length
e_eff = 3.31    # effective dielectric constant

file_reactance = open('sim_TRL_reflect_z_img.csv', 'rb')  # open the file for reading
reactance = csv.reader(file_reactance, delimiter=',')   # convert cvs file to python list
file_capacitance = open('sim_TRL_refelect_cap.csv', 'wb') # open the file for writing
capacitance = csv.writer(file_capacitance, delimiter=',')   # convert cvs file to python list

pi = np.pi

# extract information from csv and store in the following lists for plotting and processing
freq = []
reflect_cap = []
z_img = []

for row in reactance:   # row contains the row data
    if reactance.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        z_img.append(float(row[1]))     # original z_img for plotting purpose only
        row[0] = float(row[0])*1e9    # convert frequency from GHz to Hz
        row[1] = 1/(2*pi*row[0]*-1*float(row[1]))  # convert reactance to capacitance in F
        freq.append(row[0])
        reflect_cap.append(row[1])
        capacitance.writerow(row)

# debug

# poly fit reflect_cap data
z = np.polyfit(freq, reflect_cap, 3)  # use 3 degree poly

# convert the coefficients to corresponding unit from VNA
# higher order first
print 'raw coefficients: ' + str(z)
c3 = z[0]/1e-45
c2 = z[1]/1e-36
c1 = z[2]/1e-27
c0 = z[3]/1e-15

print 'Reflect Standard Parameters: '
print 'C0: %e' % c0
print 'C1: %e' % c1
print 'C2: %e' % c2
print 'C3: %e' % c3

# turn poly coefficient into a function to compare
p = np.poly1d(z)
# print 'test polyfit equation1: %f' %p(freq[0])  # test
# print 'test polyfit equation2: %f' %p(freq[len(freq)-1])  # test

reflect_cap_polyfit = []
for i in range(0, len(freq)):
    reflect_cap_polyfit.append(p(freq[i]))    # create data set for comparison

plot.figure(1)
ax0 = plot.subplot(211)
ax0.plot(freq, reflect_cap, 'r-', label="simulated capacitance")
ax0.plot(freq, reflect_cap_polyfit, 'b-', label="poly-fit capacitance")
# ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('reflect standard capacitance (F)')
plot.title('TRL reflect standard capacitance')
plot.legend(loc=4)  # loc=4 => bottom right corner

ax1 = plot.subplot(212)
ax1.plot(freq, z_img, 'r-', label="simulated reflect_z_img")
# ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('reflect standard z_img')
plot.title('TRL reflect standard z_img')
plot.legend(loc=4)  # loc=4 => bottom right corner

plot.show()

file_capacitance.close()
file_reactance.close()
