import numpy as np
import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []      #frequency
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []     
y6 = []     
y7 = []
y8 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Milled_Hybrid_S11.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        x.append(float(row['Freq(Hz)']))
        y1.append(float(row['S11 Log Mag(dB)']))
        y2.append(float(row['S21 Log Mag(dB)']))
        y3.append(float(row['S31 Log Mag(dB)']))
        y4.append(float(row['S41 Log Mag(dB)']))
        y5.append(float(row['S11_HFSS']))
        y6.append(float(row['S21_HFSS']))
        y7.append(float(row['S31_HFSS']))
        y8.append(float(row['S41_HFSS']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, 'b', label="S11 Meas") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(x, y5, 'b--', label="S11 Sim")

ax1.plot(x, y2, 'g', label="S21 Meas")
ax1.plot(x, y6, 'g--', label="S21 Sim")

ax1.plot(x, y3, 'r', label="S31 Meas")
ax1.plot(x, y7, 'r--', label="S31 Sim")

ax1.plot(x, y4, 'c', label="S41 Meas")
ax1.plot(x, y8, 'c--', label="S41 Sim")

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #1 (top-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Hybrid Coupler Magnitude') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Magnitude [dB]') #add y-axis title

plt.show() #required to display plots