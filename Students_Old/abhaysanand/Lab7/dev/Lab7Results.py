import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
S11_Milled_WPD_dB = []
S22_Milled_WPD_dB = []
S33_Milled_WPD_dB = []
S21_Milled_WPD_dB = []
S31_Milled_WPD_dB = []
S32_Milled_WPD_dB = []

S11_Sim_WPD_dB = []
S22_Sim_WPD_dB = []
S33_Sim_WPD_dB = []
S21_Sim_WPD_dB = []
S31_Sim_WPD_dB = []
S32_Sim_WPD_dB = []

S11_PS_Thru_dB = []
S21_PS_Thru_dB = []
S11_PS_Thru_phase = []
S21_PS_Thru_phase = []

S11_PS_Thru2_dB = []
S21_PS_Thru2_dB = []
S11_PS_Thru2_phase = []
S21_PS_Thru2_phase = []

S11_PS_90_dB = []
S21_PS_90_dB = []
S11_PS_90_phase = []
S21_PS_90_phase = []

S11_PS_180_dB = []
S21_PS_180_dB = []
S11_PS_180_phase = []
S21_PS_180_phase = []

freq = []

####################### MEASURED DATA ################################
# Read S11 of WPD Milled measured data dB
with open('MeasuredData/Milled_Wilkinson_S11.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_Milled_WPD_dB.append(float(row['S11 Log Mag(dB)']))

# Read S22 of WPD Milled measured data dB
with open('MeasuredData/Milled_Wilkinson_S22.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S22_Milled_WPD_dB.append(float(row['S11 Log Mag(dB)']))
        
# Read S33 of WPD Milled measured data dB
with open('MeasuredData/Milled_Wilkinson_S33.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S33_Milled_WPD_dB.append(float(row['S11 Log Mag(dB)']))

# Read S21 of WPD Milled measured data dB
with open('MeasuredData/Milled_Wilkinson_S21.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S21_Milled_WPD_dB.append(float(row['S21 Log Mag(dB)']))
        
# Read S31 of WPD Milled measured data dB
with open('MeasuredData/Milled_Wilkinson_S31.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S31_Milled_WPD_dB.append(float(row['S21 Log Mag(dB)']))

# Read S32 of WPD Milled measured data dB
with open('MeasuredData/Milled_Wilkinson_S32.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S32_Milled_WPD_dB.append(float(row['S21 Log Mag(dB)']))

# Read Thru of Phase shifter measured data dB and Phase
with open('MeasuredData/AA_SJ_THRU.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_PS_Thru_dB.append(float(row['S11 Log Mag(dB)']))
        S21_PS_Thru_dB.append(float(row['S21 Log Mag(dB)']))
        S11_PS_Thru_phase.append(float(row['S11 Phase']))
        S21_PS_Thru_phase.append(float(row['S21 Phase']))

# Read Thru Coupled of Phase shifter measured data dB and Phase
with open('MeasuredData/AA_SJ_THRU2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_PS_Thru2_dB.append(float(row['S11 Log Mag(dB)']))
        S21_PS_Thru2_dB.append(float(row['S21 Log Mag(dB)']))
        S11_PS_Thru2_phase.append(float(row['S11 Phase']))
        S21_PS_Thru2_phase.append(float(row['S21 Phase']))

# Read 90 of Phase shifter measured data dB and Phase
with open('MeasuredData/AA_SJ_90deg.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_PS_90_dB.append(float(row['S11 Log Mag(dB)']))
        S21_PS_90_dB.append(float(row['S21 Log Mag(dB)']))
        S11_PS_90_phase.append(float(row['S11 Phase']))
        S21_PS_90_phase.append(float(row['S21 Phase']))

# Read 180 of Phase shifter measured data dB and Phase
with open('MeasuredData/AA_SJ_180deg.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        S11_PS_180_dB.append(float(row['S11 Log Mag(dB)']))
        S21_PS_180_dB.append(float(row['S21 Log Mag(dB)']))
        S11_PS_180_phase.append(float(row['S11 Phase']))
        S21_PS_180_phase.append(float(row['S21 Phase']))

####################### Simulated DATA ################################
# Read S11 and S21 of LPF simulated data dB
with open('WPD_Sim_SParam_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq [GHz]']))
        S11_Sim_WPD_dB.append(float(row['dB(S(1,1)) []']))
        S22_Sim_WPD_dB.append(float(row['dB(S(2,2)) []']))
        S33_Sim_WPD_dB.append(float(row['dB(S(3,3)) []']))
        S21_Sim_WPD_dB.append(float(row['dB(S(2,1)) []']))
        S31_Sim_WPD_dB.append(float(row['dB(S(3,1)) []']))
        S32_Sim_WPD_dB.append(float(row['dB(S(3,2)) []']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)
ax1.plot(freq, S11_Milled_WPD_dB, '-r', label="S11 Milled")
ax1.plot(freq, S22_Milled_WPD_dB, '-g', label="S22 Milled")
ax1.plot(freq, S33_Milled_WPD_dB, '-b', label="S33 Milled")
ax1.plot(freq, S11_Sim_WPD_dB, '--r', label="S11 Simulated")
ax1.plot(freq, S22_Sim_WPD_dB, '--g', label="S22 Simulated")
ax1.plot(freq, S33_Sim_WPD_dB, '--b', label="S33 Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('WPD Port Reflections - S Parameters')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('[dB]')  # add y-axis title
plt.tight_layout()

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(111)
ax1.plot(freq, S21_Milled_WPD_dB, '-r', label="S21 Milled")
ax1.plot(freq, S31_Milled_WPD_dB, '-g', label="S31 Milled")
ax1.plot(freq, S21_Sim_WPD_dB, '--r', label="S21 Simulated")
ax1.plot(freq, S31_Sim_WPD_dB, '--g', label="S31 Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-5, 1)  # set x-axis limits
ax1.legend(loc=1)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('WPD Port Transmission - S Parameters')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('[dB]')  # add y-axis title
plt.tight_layout()

plt.figure(3)  # initialize plot3
ax1 = plt.subplot(111)
ax1.plot(freq, S32_Milled_WPD_dB, '-r', label="S32 Milled")
ax1.plot(freq, S32_Sim_WPD_dB, '--r', label="S32 Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('WPD Port Isolation - S Parameters')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('[dB]')  # add y-axis title
plt.tight_layout()

plt.figure(4)  # initialize plot4
ax1 = plt.subplot(221)
ax1.plot(freq, S11_PS_Thru_dB, '-r', label="S11 Thru")
ax1.plot(freq, S11_PS_Thru2_dB, '-g', label="S11 Thru + Coupled")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter THRU S11 magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

ax1 = plt.subplot(222)
ax1.plot(freq, S11_PS_Thru_phase, '-r', label="S11 Thru")
ax1.plot(freq, S11_PS_Thru2_phase, '-g', label="S11 Thru + Coupled")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-50, 450)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter THRU S11 phase')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [degrees]')  # add y-axis title

ax1 = plt.subplot(223)
ax1.plot(freq, S21_PS_Thru_dB, '-r', label="S21 Thru")
ax1.plot(freq, S21_PS_Thru2_dB, '-g', label="S21 Thru + Coupled")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-10, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter THRU S21 magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(224)
ax1.plot(freq, S21_PS_Thru_phase, '-r', label="S21 Thru")
ax1.plot(freq, S21_PS_Thru2_phase, '-g', label="S21 Thru + Coupled")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-800, 0)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter THRU S21 phase')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [degrees]')  # add y-axis title
plt.tight_layout()

plt.figure(5)  # initialize plot5
ax1 = plt.subplot(221)
ax1.plot(freq, S11_PS_90_dB, '-r', label="S11 90 degrees")
ax1.plot(freq, S11_PS_180_dB, '-g', label="S11 180 degrees")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-60, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter 90 and 180 - S11 magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [dB]')  # add y-axis title

ax1 = plt.subplot(222)
ax1.plot(freq, S11_PS_90_phase, '-r', label="S11 90 degrees")
ax1.plot(freq, S11_PS_180_phase, '-g', label="S11 180 degrees")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-800, 0)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter 90 and 180 - S11 phase')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S11 [degrees]')  # add y-axis title

ax1 = plt.subplot(223)
ax1.plot(freq, S21_PS_90_dB, '-r', label="S21 90 degrees")
ax1.plot(freq, S21_PS_180_dB, '-g', label="S21 180 degrees")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-10, 5)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter 90 and 180 - S21 magnitude')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [dB]')  # add y-axis title

ax1 = plt.subplot(224)
ax1.plot(freq, S21_PS_90_phase, '-r', label="S21 90 degrees")
ax1.plot(freq, S21_PS_180_phase, '-g', label="S21 180 degrees")
ax1.plot(freq, S21_PS_Thru2_phase, '-b', label="S21 Thru")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(-900, 200)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Phase Shifter THRU, 90 and 180 - S21 phase')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('S21 [degrees]')  # add y-axis title
plt.tight_layout()

plt.show()  # required to display plots