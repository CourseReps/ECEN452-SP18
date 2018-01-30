import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
Phase_Difference_HFSS = []
Phase_Difference_measured = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('90deg_phase_difference_hybrid_plot.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq [GHz]']))
        Phase_Difference_HFSS.append(float(row['Phase_Difference(HFSS)']))
        Phase_Difference_measured.append(float(row['Phase_Difference(measured)']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, Phase_Difference_HFSS, '-b', label="Phase_Difference(HFSS)") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, Phase_Difference_measured, '-r', label="Phase_Difference(measured)") #plot y1 vs. x, solid-blue, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Input Port 1 90 deg phase difference for Hybrid Coupler') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Phase Difference [deg]') #add y-axis title

plt.show() #required to display plots