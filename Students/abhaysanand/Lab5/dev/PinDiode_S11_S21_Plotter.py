import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
S11_OFF_Meas_dB = []
S21_OFF_Meas_dB = []
S11_ON_Meas_dB = []
S21_ON_Meas_dB = []

S11_OFF_Sim_dB = []
S21_OFF_Sim_dB = []
S11_ON_Sim_dB = []
S21_ON_Sim_dB = []

freq = []

####################### MEASURED DATA ################################
# Read S11 and S21 PinDiode OFF dB measured data
with open('S11_S21_OFF_dB_Meas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_OFF_Meas_dB.append(float(row['S11 Log Mag(dB)']))
        S21_OFF_Meas_dB.append(float(row['S21 Log Mag(dB)']))

# Read S11 and S21 PinDiode ON dB measured data
with open('S11_S21_ON_dB_Meas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_ON_Meas_dB.append(float(row['S11 Log Mag(dB)']))
        S21_ON_Meas_dB.append(float(row['S21 Log Mag(dB)']))

####################### Simulated DATA ################################
# Read S11 and S21 PinDiode OFF dB simulated data
with open('S11_S21_OFF_dB_Sim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq [GHz]']))
        S11_OFF_Sim_dB.append(float(row['dB(S(1,1))']))
        S21_OFF_Sim_dB.append(float(row['dB(S(2,1))']))

# Read S21 Line Phase measured data
with open('S11_S21_ON_dB_Sim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S11_ON_Sim_dB.append(float(row['dB(S(1,1))']))
        S21_ON_Sim_dB.append(float(row['dB(S(2,1))']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(221)  # create axes handle for plot1
ax1.plot(freq, S11_OFF_Sim_dB, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S11_OFF_Meas_dB, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-30, 5)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('OFF - S11')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

ax1 = plt.subplot(222)  # create axes handle for plot1
ax1.plot(freq, S11_ON_Sim_dB, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S11_ON_Meas_dB, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-30, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('ON - S11')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

plt.figure(1)  # initialize plot1
ax1 = plt.subplot(223)  # create axes handle for plot1
ax1.plot(freq, S21_OFF_Sim_dB, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S21_OFF_Meas_dB, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-30, 5)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('OFF - S21')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(224)  # create axes handle for plot1
ax1.plot(freq, S21_ON_Sim_dB, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S21_ON_Meas_dB, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-30, 5)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('ON - S21')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

plt.tight_layout()
plt.show()  # required to display plots
