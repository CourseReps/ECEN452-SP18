import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
VSWR_CuTape_Unmatched = []
VSWR_CuTape_Matched = []
VSWR_Sim = []

freq = []

####################### MEASURED DATA ################################
# Read VSWR of Unmatched CuTape Antenna
with open('MeasuredData/MM_AA_SJ_Unmatched.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        VSWR_CuTape_Unmatched.append(float(row['S11 SWR(U)']))

# Read VSWR of Matched CuTape Antenna
with open('MeasuredData/MM_AA_SJ_Stub.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        VSWR_CuTape_Matched.append(float(row['S11 SWR(U)']))

####################### Simulated DATA ################################
# Read VSWR of Simulated Matched Antenna
with open('VSWR_Antenna.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['Freq [GHz]']))
        VSWR_Sim.append(float(row['VSWR(1) []']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)
ax1.plot(freq, VSWR_CuTape_Unmatched, '--r', label="Unmatched")
ax1.plot(freq, VSWR_CuTape_Matched, '-r', label="Stub Matched")
ax1.plot(freq, VSWR_Sim, '-g', label="Simulated")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(1, 5)  # set x-axis limits
ax1.legend(loc=2)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('VSWR of Patch Antennas')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('VSWR')  # add y-axis title

plt.tight_layout()

plt.show()  # required to display plots