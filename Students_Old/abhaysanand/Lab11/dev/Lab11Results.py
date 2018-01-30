import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
S11_TD_wReflect_preGRLcal = []
S21_Thru_postGRL = []
Air = []
Cardboard = []
Plexiglass = []

freq = []
time = []

####################### MEASURED DATA ################################
with open('S11_TD_wReflect_preGRLcal.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time.append(float(row['Time(ns)']))
        S11_TD_wReflect_preGRLcal.append(float(row['S11 Log Mag(dB)']))

with open('S21_Thru_postGRL.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq(GHz)']))
        S21_Thru_postGRL.append(float(row['S21 Log Mag(dB)']))

with open('Air.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Air.append(float(row['e\'']))

with open('Cardboard.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Cardboard.append(float(row['e\'']))

with open('Plexiglass.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Plexiglass.append(float(row['e\'']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)
ax1.plot(time, S11_TD_wReflect_preGRLcal, '-r', label='S11')
ax1.set_xlim(min(time), max(time))  # set x-axis limits
ax1.set_ylim(-120, 0)  # set x-axis limits
ax1.legend(loc=1)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('S11 Time Domain with Reflect - Pre calibration')  # add plot title
plt.xlabel('Time [ns]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

plt.tight_layout()

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(111)
ax1.plot(freq, S21_Thru_postGRL, '-r', label='S21')
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-10, 0.5)  # set x-axis limits
ax1.legend(loc=1)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('S21 - Post calibration')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

plt.tight_layout()

plt.figure(3)  # initialize plot3
ax1 = plt.subplot(111)
ax1.plot(freq, Air, '-r', label="Air")
ax1.plot(freq, Cardboard, '-g', label="Cardboard")
ax1.plot(freq, Plexiglass, '-b', label="Plexiglass")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(0, 4)  # set x-axis limits
ax1.legend(loc=1)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Dielectric Constant - GRL Measurement')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('e\'')  # add y-axis title

plt.tight_layout()



plt.show()  # required to display plots