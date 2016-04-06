import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
S11_milled = []
S11_HFSS = []
S11_z0lver = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Milled_Wilkinson_Phase.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq(Hz)']))
        S11_milled.append(float(row['S11_Phase']))
        S11_HFSS.append(float(row['S22_Phase']))
        S11_z0lver.append(float(row['S33_Phase']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, S11_milled, '-b', label="S11 Phase") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, S11_HFSS, '-r', label="S22 Phase") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, S11_z0lver, '-k', label="S33 Phase") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.legend(loc=3) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Wilkinson Power Divider - Phase S11, S22, S33') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Phase [deg]') #add y-axis title

plt.show() #required to display plots