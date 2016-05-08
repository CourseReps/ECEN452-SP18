import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
DI_Water = []
DI_water_20MHz_20GHz = []
Acetone = []
Ethylene_Glycol = []
Glass_Cleaner = []
Hydrocal = []
Isopropyl_Alcohol = []
Pine_sol = []
Silicone_Fluid = []
Simple_Green = []
WD_40 = []

freq = []
freq20 = []

####################### MEASURED DATA ################################
with open('DI_Water.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq.append(float(row['frequency']))
        DI_Water.append(float(row['e\'']))

with open('Acetone.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Acetone.append(float(row['e\'']))

with open('Ethylene_Glycol.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Ethylene_Glycol.append(float(row['e\'']))

with open('Glass_Cleaner.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Glass_Cleaner.append(float(row['e\'']))

with open('Hydrocal.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Hydrocal.append(float(row['e\'']))

with open('Isopropyl_Alcohol.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Isopropyl_Alcohol.append(float(row['e\'']))

with open('Pine_sol.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Pine_sol.append(float(row['e\'']))

with open('Silicone_Fluid.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Silicone_Fluid.append(float(row['e\'']))

with open('Simple_Green.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Simple_Green.append(float(row['e\'']))

with open('WD_40.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        WD_40.append(float(row['e\'']))

with open('DI_water_20MHz_20GHz.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        freq20.append(float(row['frequency']))
        DI_water_20MHz_20GHz.append(float(row['e\'']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)
ax1.plot(freq, DI_Water, '-r', label="DI Water")
ax1.plot(freq, Glass_Cleaner, '--r', label="Glass Cleaner")
ax1.plot(freq, Ethylene_Glycol, '-b', label="Ethylene Glycol")
ax1.plot(freq, Isopropyl_Alcohol, '--b', label="Isopropyl Alcohol")
ax1.plot(freq, Hydrocal, '-y', label="Hydrocal")
ax1.plot(freq, Silicone_Fluid, '--y', label="Silicone Fluid")
ax1.plot(freq, WD_40, '-.y', label="WD-40")
ax1.plot(freq, Pine_sol, '-c', label="Pine Sol")
ax1.plot(freq, Simple_Green, '--c', label="Simple Green")
ax1.plot(freq, Acetone, '-g', label="Acetone")
ax1.set_xlim(min(freq), max(freq))  # set x-axis limits
ax1.set_ylim(0, 80)  # set x-axis limits
ax1.legend(loc=2)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Dielectric Constant - Liquids')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('e\'')  # add y-axis title

plt.tight_layout()

plt.figure(2)  # initialize plot2
ax1 = plt.subplot(111)
ax1.plot(freq20, DI_water_20MHz_20GHz, '-r', label="DI Water")
ax1.set_xlim(min(freq20), max(freq20))  # set x-axis limits
ax1.set_ylim(40, 80)  # set x-axis limits
ax1.legend(loc=3)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Dielectric Constant - DI Water')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('e\'')  # add y-axis title

plt.tight_layout()

plt.show()  # required to display plots