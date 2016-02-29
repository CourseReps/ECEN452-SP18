# import matplotlib.pyplot as plt
import csv
import numpy as np

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for freq, phase
freq = []
phase = []

# Read .csv data file
with open('TRL_Demo_Line_S21_Phase.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Freq(Hz)'] == 'END':
            break
        # Convert all Hz to GHz scale
        freq.append(float(row['Freq(Hz)'])/1e9)
        phase.append(float(row['S21 Phase(deg)']))

# Linear polynomial fit
polyPhase = np.polyfit(freq, phase, 1)
# The resultant array is of the form [m, c] where y = mx + c
# Reverse the equation to solve or x => change to x = (y-c)/m
x = np.poly1d([1/polyPhase[0], -polyPhase[1]/polyPhase[0]])

print("Frequency Minimum = %f GHz" % x(-20))
print("Frequency Maximum = %f GHz" % x(-160))
