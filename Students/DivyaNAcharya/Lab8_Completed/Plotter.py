import matplotlib.pyplot as plt
import csv
import numpy as np

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
M = []
CT = []
HFSS = []
Y = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Angle_Hybrid.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq']))
        M.append(float(row['S1M']))
        CT.append(float(row['S4M']))
        M1.append(float(row['S1H']))
        CT1.append(float(row['S4H']))


##Plotting
yticks=[0,30,60,80,90,100,120,150,180,210]
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, M, '-b', label="Milled: Input at port 1") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, CT, '-r', label="Milled: Input at port 4") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, M2, '--b', label="HFSS: Input at port 1") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, CT2, '--r', label="HFSS: Input at port 4") #plot y2 vs. x, solid-red, add lable for legend

ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
#ax1.set_ylim(-200,10) #set y-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Phase difference between output at ports 2 and 3') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Phase [degrees]') #add y-axis title
plt.axvline(x=2.5, ymin=0, ymax=1, hold=None)
plt.yticks(yticks)
plt.show() #required to display plots