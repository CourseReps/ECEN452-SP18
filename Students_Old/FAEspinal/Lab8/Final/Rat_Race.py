import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for Freq, S21_HFSS, S31_HFSS, S41_HFSS, S21_Milled, S31_Milled, S41_Milled
Freq = []
S21_HFSS = []
S31_HFSS = []
S41_HFSS = []
S21_Milled = []
S31_Milled = []
S41_Milled = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Rat_Race_Magnitude.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        Freq.append(float(row['Freq']))
        S21_HFSS.append(float(row['S21_HFSS']))
        S31_HFSS.append(float(row['S31_HFSS']))
        S41_HFSS.append(float(row['S41_HFSS']))
        S21_Milled.append(float(row['S21_Milled']))
        S31_Milled.append(float(row['S31_Milled']))
        S41_Milled.append(float(row['S41_Milled']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(Freq, S21_HFSS, '-b', label="S21_HFSS Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, S31_HFSS, '-r', label="S31_HFSS Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, S41_HFSS, '-c', label="S41_HFSS Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, S21_Milled, '-y', label="S21_Milled Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, S31_Milled, '-k', label="S31_Milled Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, S41_Milled, '--k', label="S41_Milled Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(Freq), max(Freq)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Rat Race') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Magnitude') #add y-axis title


plt.show() #required to display plots