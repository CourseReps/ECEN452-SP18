import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
S11_Milled_LPF_dB = []
S21_Milled_LPF_dB = []
S11_Milled_BSF_dB = []
S21_Milled_BSF_dB = []
S11_Milled_BSF_phase = []
S21_Milled_BSF_phase = []

S11_CuTape_BSF_dB = []
S21_CuTape_BSF_dB = []
S11_CuTape_BSF_phase = []
S21_CuTape_BSF_phase = []

S11_Sim_LPF_dB = []
S21_Sim_LPF_dB = []
S11_Sim_LPF_TapStub_dB = []
S21_Sim_LPF_TapStub_dB = []
S11_Sim_BSF_dB = []
S21_Sim_BSF_dB = []
S11_Sim_BSF_phase = []
S21_Sim_BSF_phase = []

freq = []

####################### MEASURED DATA ################################
# Read S11 and S21 of LPF Milled measured data dB
with open('MeasuredData/Milled_LPF_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_Milled_LPF_dB.append(float(row['S11 Log Mag(dB)']))
        S21_Milled_LPF_dB.append(float(row['S21 Log Mag(dB)']))

# Read S11 and S21 of BSF Milled measured data dB
with open('MeasuredData/Milled_BSF_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_Milled_BSF_dB.append(float(row['S11 Log Mag(dB)']))
        S21_Milled_BSF_dB.append(float(row['S21 Log Mag(dB)']))

# Read S11 and S21 of BSF Milled measured data phase
with open('MeasuredData/Milled_BSF_phase.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_Milled_BSF_phase.append(float(row['S11 Phase']))
        S21_Milled_BSF_phase.append(float(row['S21 Phase']))

# Read S11 and S21 of BSF Copper Tape measured data dB
with open('MeasuredData/AA_SJ_BSF_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_CuTape_BSF_dB.append(float(row['S11 Log Mag(dB)']))
        S21_CuTape_BSF_dB.append(float(row['S21 Log Mag(dB)']))

# Read S11 and S21 of BSF Copper Tape measured data phase
with open('MeasuredData/AA_SJ_BSF_phase.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_CuTape_BSF_phase.append(float(row['S11 Phase']))
        S21_CuTape_BSF_phase.append(float(row['S21 Phase']))

####################### Simulated DATA ################################
# Read S11 and S21 of LPF simulated data dB
with open('LPF_Sim_TL_S11_S21_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq [GHz]']))
        S11_Sim_LPF_dB.append(float(row['dB(S(1,1)) []']))
        S21_Sim_LPF_dB.append(float(row['dB(S(2,1)) []']))

# Read S11 and S21 of LPF Tapped Stub simulated data dB
with open('LPF_Sim_TL_TapStub_S11_S21_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S11_Sim_LPF_TapStub_dB.append(float(row['dB(S(1,1)) []']))
        S21_Sim_LPF_TapStub_dB.append(float(row['dB(S(2,1)) []']))

# Read S11 and S21 of BSF simulated data dB and phase
with open('BSF_Sim_TL_SParam.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        S11_Sim_BSF_dB.append(float(row['dB(S(1,1)) []']))
        S11_Sim_BSF_phase.append(float(row['ang_deg(S(1,1)) [deg]']))
        S21_Sim_BSF_dB.append(float(row['dB(S(2,1)) []']))
        S21_Sim_BSF_phase.append(float(row['ang_deg(S(2,1)) [deg]']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(211)
ax1.plot(freq, S11_Sim_LPF_dB, '-r', label="Traditinal - Sim")
ax1.plot(freq, S11_Sim_LPF_TapStub_dB, '-g', label="Tapped Stub - Sim")
ax1.plot(freq, S11_Milled_LPF_dB, '--b', label="Milled")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('LPF filters comparison - S11[dB]')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

plt.figure(1)  # initialize plot1
ax1 = plt.subplot(212)
ax1.plot(freq, S21_Sim_LPF_dB, '-r', label="Traditinal - Sim")
ax1.plot(freq, S21_Sim_LPF_TapStub_dB, '-g', label="Tapped Stub - Sim")
ax1.plot(freq, S21_Milled_LPF_dB, '--b', label="Milled")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('LPF filters comparison - S21[dB]')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

plt.tight_layout()

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(221)
ax1.plot(freq, S11_Sim_BSF_dB, '-r', label="Sim")
ax1.plot(freq, S11_Milled_BSF_dB, '--g', label="Milled")
ax1.plot(freq, S11_CuTape_BSF_dB, '--b', label="Coppper Tape")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('BSF filters comparison - S11[dB]')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(222)
ax1.plot(freq, S11_Sim_BSF_phase, '-r', label="Sim")
ax1.plot(freq, S11_Milled_BSF_phase, '--g', label="Milled")
ax1.plot(freq, S11_CuTape_BSF_phase, '--b', label="Coppper Tape")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-180, 180)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('BSF filters comparison - S11[degrees]')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [degrees]')  # add y-axis title

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(223)
ax1.plot(freq, S21_Sim_BSF_dB, '-r', label="Sim")
ax1.plot(freq, S21_Milled_BSF_dB, '--g', label="Milled")
ax1.plot(freq, S21_CuTape_BSF_dB, '--b', label="Coppper Tape")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('BSF filters comparison - S21[dB]')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(224)
ax1.plot(freq, S21_Sim_BSF_phase, '-r', label="Sim")
ax1.plot(freq, S21_Milled_BSF_phase, '--g', label="Milled")
ax1.plot(freq, S21_CuTape_BSF_phase, '--b', label="Coppper Tape")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-180, 180)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('BSF filters comparison - S21[degrees]')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [degrees]')  # add y-axis title

plt.tight_layout()
plt.show()  # required to display plots
