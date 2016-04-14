import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
VSWR_HFSS = []
VSWR_measured_stub_matching = []
VSWR_measured_unmatched = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('VSWR_plot.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq [GHz]']))
        VSWR_HFSS.append(float(row['VSWR_HFSS']))
        VSWR_measured_stub_matching.append(float(row['VSWR_measured_stub_matching']))
        VSWR_measured_unmatched.append(float(row['VSWR_measured_unmatched']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, VSWR_HFSS, '-b', label="VSWR_HFSS_Probe_Fed") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, VSWR_measured_stub_matching, '-r', label="VSWR_measured_stub") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, VSWR_measured_unmatched, '-g', label="VSWR_measured_unmatched") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.set_ylim(1, 5) #set x-axis limits
ax1.legend(loc=2) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('VSWR') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('VSWR') #add y-axis title

plt.show() #required to display plots