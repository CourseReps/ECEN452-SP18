import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
S21_Line_Meas_dB = []
S21_Line_Meas_phase = []
S21_Thru_Meas_dB = []
S21_Thru_Meas_phase = []

S21_Line_Sim_dB = []
S21_Line_Sim_phase = []
S21_Thru_Sim_dB = []
S21_Thru_Sim_phase = []

freq = []

####################### MEASURED DATA ################################
# Read S21 Line dB measured data
with open('S21_Line_dB_Meas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Line_Meas_dB.append(float(row['S21 Log Mag(dB)']))

# Read S21 Line Phase measured data
with open('S21_Line_Phase_Meas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Line_Meas_phase.append(float(row['S21 Phase']))

# Read S21 Thru dB measured data
with open('S21_Thru_dB_Meas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Thru_Meas_dB.append(float(row['S21 Log Mag(dB)']))

# Read S21 Thru Phase measured data
with open('S21_Thru_Phase_Meas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Thru_Meas_phase.append(float(row['S21 Phase']))

####################### Simulated DATA ################################
# Read S21 Line dB measured data
with open('S11_S21_Line_dB_Sim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq [GHz]']))
        S21_Line_Sim_dB.append(float(row['dB(S(2,1)) []']))

# Read S21 Line Phase measured data
with open('S11_S21_Line_phase_Sim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S21_Line_Sim_phase.append(float(row['cang_deg(S(2,1)) [deg]']))

# Read S21 Thru dB measured data
with open('S11_S21_Thru_dB_Sim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S21_Thru_Sim_dB.append(float(row['dB(S(2,1)) []']))

# Read S21 Thru Phase measured data
with open('S11_S21_Thru_phase_Sim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S21_Thru_Sim_phase.append(float(row['cang_deg(S(2,1)) [deg]']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(221)  # create axes handle for plot1
ax1.plot(freq, S21_Line_Sim_dB, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S21_Line_Meas_dB, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-40, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Line - S21 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(222)  # create axes handle for plot1
ax1.plot(freq, S21_Line_Sim_phase, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S21_Line_Meas_phase, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-160, -20)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Line - S21 Phase')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [degrees]')  # add y-axis title

plt.figure(1)  # initialize plot1
ax1 = plt.subplot(223)  # create axes handle for plot1
ax1.plot(freq, S21_Thru_Sim_dB, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S21_Thru_Meas_dB, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-40, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Thru - S21 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(224)  # create axes handle for plot1
ax1.plot(freq, S21_Thru_Sim_phase, '-r', label="Simulated")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(freq, S21_Thru_Meas_phase, '--b', label="Measured")  # plot y1 vs. x, solid-blue, add label for legend
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-10, 10)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Thru - S21 Phase')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [degrees]')  # add y-axis title

plt.tight_layout()
plt.show()  # required to display plots
