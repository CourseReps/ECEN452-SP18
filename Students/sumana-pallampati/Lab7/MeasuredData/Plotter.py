import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
S11_90deg = []
S11_180deg = []
S11_thru = []
S11_thru_with_coupling = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('S21_Phase.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq(Hz)']))
        S11_90deg.append(float(row['S21_Phase_90deg']))
        S11_180deg.append(float(row['S21_Phase_180deg']))
        S11_thru.append(float(row['S21_Phase_thru']))
        S11_thru_with_coupling.append(float(row['S21_Phase_thru_with_coupling']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, S11_90deg, '-b', label="S21 Phase 90deg") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, S11_180deg, '-r', label="S21 Phase 180deg") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, S11_thru, '-k', label="S21 Phase thru") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, S11_thru_with_coupling, '-c', label="S21 Phase thru with coupling")
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.legend(loc=3) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Phase Shifter - S21 Phase') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Phase [deg]') #add y-axis title

plt.show() #required to display plots