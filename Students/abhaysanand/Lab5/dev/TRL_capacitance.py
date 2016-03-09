# import matplotlib.pyplot as plt
import csv
import numpy as np
import math
import matplotlib.pyplot as plt

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

f0 = 3e9;
phase = 90.7864 # phase of TRL line at 3GHz in degrees
line_length = 13.95e-3 # additional line length in meters
c = 3e8 # speed of light in mps

eeff = (c * phase / (f0*line_length*360))**2 # effective dielectric constane calculation
vp = c/math.sqrt(eeff) # phase velocity in mps
delay = line_length/vp # delay caused due to the excess line length
delay = delay/1e-12 # convert s to ps
print('Delay = ', delay, 'ps')
# Initialize arrays for freq, phase
freq = []
imZ = []
cap = []

# Read .csv data file
with open('ImZ_SimReflect.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq [GHz]'] == 'END':
            break
        # Convert all Hz to GHz scale
        freq.append(float(row['Freq [GHz]']))
        imZ.append(float(row['im(Z(1,1)) []']))
        cap.append(float(-1e6 / (2*math.pi*float(row['im(Z(1,1)) []'])*float(row['Freq [GHz]']))))

# Linear polynomial fit
polyCap = np.polyfit(freq, cap, 3)
print('C0 = ',polyCap[3])
print('C1 = ',polyCap[2])
print('C2 = ',polyCap[1])
print('C3 = ',polyCap[0])

# Converting the coefficients into an equation
p = np.poly1d(polyCap)

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)  # create axes handle for plot1
ax1.plot(freq, cap, '-b', label="Simulated")  # plot capacitance vs. Frequency
ax1.plot(freq, p(freq), '--r', label='Curve Fit') # plot curve-fit capacitance vs frequency
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('TRL Capacitance')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('Capacitance [pF]')  # add y-axis title

plt.show()  # required to display plots