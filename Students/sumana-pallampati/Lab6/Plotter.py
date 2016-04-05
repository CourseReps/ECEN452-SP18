import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
S11_HFSS = []
S11_milled = []
S11_z0lver = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('LPF_tapped_phase_S11.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq(Hz)']))
        S11_HFSS.append(float(row['S11 Phase_HFSS']))
        S11_milled.append(float(row['S11 Phase_milled']))
        S11_z0lver.append(float(row['S11 Phase_z0lver']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, S11_HFSS, '-r', label="S11 (phase) HFSS") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, S11_milled, '-g', label="S11 (phase) Milled") #plot y3 vs. x, dashed-red, add lable for legend
ax1.plot(f1, S11_z0lver, '-k', label="S11 (phase) Z0lver") #plot y3 vs. x, dashed-blue, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.set_ylim(-180,180) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('S11 (phase) of Low Pass Filter') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('S11 [deg]') #add y-axis title

plt.show() #required to display plots