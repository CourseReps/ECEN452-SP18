import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []
y1 = []
y2 = []
y3 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('ECEN_452_lab1_s11_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        x.append(float(row['Frequency (GHz)']))
        y1.append(float(row['Analytical (S11 dB)']))
        y2.append(float(row['Z0lver (S11 dB)']))
        y3.append(float(row['HFSS (S11 dB)']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, '-b', label="Analytical") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(x, y2, '-r', label="Z0lver") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y3, '--r', label="HFSS") #plot y3 vs. x, dashed-red, add lable for legend
ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('S11') #add plot title
plt.xlabel('f (GHz)') #add x-axis title
plt.ylabel('Magnitude (dB)') #add y-axis title

plt.show() #required to display plots