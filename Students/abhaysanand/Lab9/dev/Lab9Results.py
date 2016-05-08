import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
S11_Milled_HC_dB = []
S21_Milled_HC_dB = []
S31_Milled_HC_dB = []
S41_Milled_HC_dB = []

S21_Milled_HC_phase = []
S31_Milled_HC_phase = []

S11_Sim_HC_dB = []
S21_Sim_HC_dB = []
S31_Sim_HC_dB = []
S41_Sim_HC_dB = []

S21_S31_Sim_HC_phase = []

S11_Milled_RRC_dB = []
S21_Milled_RRC_dB = []
S31_Milled_RRC_dB = []
S41_Milled_RRC_dB = []

S11_Sim_RRC_dB = []
S21_Sim_RRC_dB = []
S31_Sim_RRC_dB = []
S41_Sim_RRC_dB = []

freq = []

####################### MEASURED DATA ################################
# Read S11 of Hybrid Coupler Milled measured data dB
with open('MeasuredData/Milled_Hybrid_S11.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_Milled_HC_dB.append(float(row['S11 Log Mag(dB)']))

# Read S21 of Hybrid Coupler Milled measured data dB
with open('MeasuredData/Milled_Hybrid_S21.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Milled_HC_dB.append(float(row['S21 Log Mag(dB)']))
        S21_Milled_HC_phase.append(float(row['S21 Phase']))

# Read S31 of Hybrid Coupler Milled measured data dB
with open('MeasuredData/Milled_Hybrid_S31.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S31_Milled_HC_dB.append(float(row['S21 Log Mag(dB)']))
        S31_Milled_HC_phase.append(float(row['S21 Phase']))

# Read S41 of Hybrid Coupler Milled measured data dB
with open('MeasuredData/Milled_Hybrid_S41.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S41_Milled_HC_dB.append(float(row['S21 Log Mag(dB)']))

# Read S11 of Rat Race Coupler Milled measured data dB
with open('MeasuredData/Milled_RatRace_S11.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_Milled_RRC_dB.append(float(row['S11 Log Mag(dB)']))

# Read S21 of Rat Race Coupler Milled measured data dB
with open('MeasuredData/Milled_RatRace_S21.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Milled_RRC_dB.append(float(row['S21 Log Mag(dB)']))

# Read S31 of Rat Race Coupler Milled measured data dB
with open('MeasuredData/Milled_RatRace_S31.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S31_Milled_RRC_dB.append(float(row['S21 Log Mag(dB)']))

# Read S41 of Rat Race Coupler Milled measured data dB
with open('MeasuredData/Milled_RatRace_S41.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S41_Milled_RRC_dB.append(float(row['S21 Log Mag(dB)']))

####################### Simulated DATA ################################
# Read S11, S21, S31 and S41 of Hybrid Coupler simulated data dB
with open('Hybrid_Sim_SParam_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq [GHz]']))
        S11_Sim_HC_dB.append(float(row['dB(S(1,1)) []']))
        S21_Sim_HC_dB.append(float(row['dB(S(2,1)) []']))
        S31_Sim_HC_dB.append(float(row['dB(S(3,1)) []']))
        S41_Sim_HC_dB.append(float(row['dB(S(4,1)) []']))

# Read S21 S31 phase difference of Hybrid Coupler degrees
with open('Hybrid_Sim_SParam_PhaseShift.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S21_S31_Sim_HC_phase.append(float(row['cang_deg(S(2,1))-cang_deg(S(3,1)) [deg]']))

# Read S11, S21, S31 and S41 of Rat Race Coupler simulated data dB
with open('RatRace_Sim_SParam_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S11_Sim_RRC_dB.append(float(row['dB(S(1,1)) []']))
        S21_Sim_RRC_dB.append(float(row['dB(S(2,1)) []']))
        S31_Sim_RRC_dB.append(float(row['dB(S(3,1)) []']))
        S41_Sim_RRC_dB.append(float(row['dB(S(4,1)) []']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(221)
ax1.plot(freq, S11_Milled_HC_dB, '-r', label="Milled")
ax1.plot(freq, S11_Sim_HC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Hybrid Coupler S11 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

ax1 = plt.subplot(222)
ax1.plot(freq, S21_Milled_HC_dB, '-r', label="Milled")
ax1.plot(freq, S21_Sim_HC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Hybrid Coupler S21 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(223)
ax1.plot(freq, S31_Milled_HC_dB, '-r', label="Milled")
ax1.plot(freq, S31_Sim_HC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Hybrid Coupler S31 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S31 [dB]')  # add y-axis title

ax1 = plt.subplot(224)
ax1.plot(freq, S41_Milled_HC_dB, '-r', label="Milled")
ax1.plot(freq, S41_Sim_HC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Hybrid Coupler S41 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S41 [dB]')  # add y-axis title
plt.tight_layout()

phaseDiff = [m - n for m,n in zip(S21_Milled_HC_phase,S31_Milled_HC_phase)]

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(111)
ax1.plot(freq, phaseDiff, '-r', label="Milled")
ax1.plot(freq, S21_S31_Sim_HC_phase, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(0, 180)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Hybrid Coupler S21-S21 Phase Difference')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('Phase [degrees]')  # add y-axis title

plt.figure(3)  # initialize plot3
ax1 = plt.subplot(221)
ax1.plot(freq, S11_Milled_RRC_dB, '-r', label="Milled")
ax1.plot(freq, S11_Sim_RRC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Rat Race Coupler S11 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

ax1 = plt.subplot(222)
ax1.plot(freq, S21_Milled_RRC_dB, '-r', label="Milled")
ax1.plot(freq, S21_Sim_RRC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Hybrid Coupler S21 Magnitude')  # add plot title
plt.xlabel('Rat Race [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(223)
ax1.plot(freq, S31_Milled_RRC_dB, '-r', label="Milled")
ax1.plot(freq, S31_Sim_RRC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Rat Race Coupler S31 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S31 [dB]')  # add y-axis title

ax1 = plt.subplot(224)
ax1.plot(freq, S41_Milled_RRC_dB, '-r', label="Milled")
ax1.plot(freq, S41_Sim_RRC_dB, '--r', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Rat Race Coupler S41 Magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S41 [dB]')  # add y-axis title
plt.tight_layout()

plt.show()  # required to display plots