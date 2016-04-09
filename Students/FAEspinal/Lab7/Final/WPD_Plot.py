import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for Freq, S11_HFSS, S22_HFSS, S33_HFSS, S11_Milled, S22_Milled, S33_Milled
Freq = []
S11_HFSS = []
S22_HFSS = []
S33_HFSS = []
S11_Milled = []
S22_Milled = []
S33_Milled = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('WPD_Matched_S_Parameter.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        Freq.append(float(row['Freq']))
        S11_HFSS.append(float(row['S11_HFSS']))
        S22_HFSS.append(float(row['S22_HFSS']))
        S33_HFSS.append(float(row['S33_HFSS']))
        S11_Milled.append(float(row['S11_Milled']))
        S22_Milled.append(float(row['S22_Milled']))
        S33_Milled.append(float(row['S33_Milled']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(Freq, S11_HFSS, '-b', label="S11_HFSS Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, S22_HFSS, '-g', label="S22_HFSS Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, S33_HFSS, '-r', label="S33_HFSS Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, S11_Milled, '-y', label="S11_Milled Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, S22_Milled, '-m', label="S22_Milled Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, S33_Milled, '-k', label="S33_Milled Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(Freq), max(Freq)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('WPD Matched S-Parameters') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Magnitude') #add y-axis title


plt.show() #required to display plots