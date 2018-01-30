import matplotlib.pyplot as plt
import csv
import numpy as np

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
M = []
CT = []
M1 = []
CT1 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('RAngles.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq']))
        M.append(float(row['SM1']))
        CT.append(float(row['SM4']))
        M1.append(float(row['SH1']))
        CT1.append(float(row['SH4']))


##Plotting
yticks=[-100,0,100,180,300,400]
yticks2=[-400,-90,0,90,180,400]
plt.figure(1) #initialize plot1
ax1 = plt.subplot(211) #create axes handle for plot1
ax1.plot(f1, M, '-b', label="Milled: Input at port 1") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, CT, '-r', label="Milled: Input at port 4") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
#ax1.set_ylim(-200,10) #set y-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Phase difference between output at ports 2 and 3') #add plot title
plt.ylabel('Phase [degrees]') #add y-axis title
plt.axvline(x=2.5, ymin=0, ymax=1, hold=None)
plt.yticks(yticks)
#plt.show() #required to display plots

ax1 = plt.subplot(212) #create axes handle for plot1
ax1.plot(f1, M1, '--b', label="HFSS: Input at port 1") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, CT1, '--r', label="HFSS: Input at port 4") #plot y2 vs. x, solid-red, add lable for legend
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Phase [degrees]') #add y-axis title
plt.axvline(x=2.5, ymin=0, ymax=1, hold=None)
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
#ax1.set_ylim(-200,10) #set y-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.yticks(yticks2)
plt.show() #required to display plots
