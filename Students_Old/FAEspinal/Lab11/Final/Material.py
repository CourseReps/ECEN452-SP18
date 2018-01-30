import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for Freq, Thru2, Thru, S180, 90
Freq = []
Air = []
Cardboard = []
Plexiglass = []


##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Material_Measurements.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        Freq.append(float(row['Freq']))
        Air.append(float(row['Air']))
        Cardboard.append(float(row['Cardboard']))
        Plexiglass.append(float(row['Plexiglass']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(Freq, Air, '-b', label="Air Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, Cardboard, '-g', label="Cardboard Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Plexiglass, '-r', label="Plexiglass Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(Freq), max(Freq)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('GRL Calibration') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Dielectric') #add y-axis title


plt.show() #required to display plots