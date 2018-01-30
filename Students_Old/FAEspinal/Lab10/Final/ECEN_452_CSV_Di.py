import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for Freq, Acetone, DI_water, Ethylene_Glycol, Glass_Cleaner, Hydrocal, Isopropyl_Alcohol, Pine_Sol,
# Silicone_Fluid, Simple_Green_Cleaner, WD_40
Freq = []
Acetone = []
DI_water = []
Ethylene_Glycol = []
Glass_Cleaner = []
Hydrocal = []
Isopropyl_Alcohol = []
Pine_Sol = []
Silicone_Fluid = []
Simple_Green_Cleaner = []
WD_40 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Dielectric_Measurments.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        Freq.append(float(row['Freq']))
        Acetone.append(float(row['Acetone']))
        DI_water.append(float(row['DI_water']))
        Ethylene_Glycol.append(float(row['Ethylene_Glycol']))
        Glass_Cleaner.append(float(row['Glass_Cleaner']))
        Hydrocal.append(float(row['Hydrocal']))
        Isopropyl_Alcohol.append(float(row['Isopropyl_Alcohol']))
        Pine_Sol.append(float(row['Pine_Sol']))
        Silicone_Fluid.append(float(row['Silicone_Fluid']))
        Simple_Green_Cleaner.append(float(row['Simple_Green_Cleaner']))
        WD_40.append(float(row['WD_40']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(Freq, Acetone, '-b', label="Acetone Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, DI_water, '-r', label="DI_water Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Ethylene_Glycol, '-c', label="Ethylene_Glycol Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Glass_Cleaner, '-m', label="Glass_Cleaner Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(Freq, Hydrocal, '-y', label="Hydrocal Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Isopropyl_Alcohol, '-r', label="Isopropyl_Alcohol Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Pine_Sol, '-k', label="Pine_Sol Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Silicone_Fluid, '--r', label="Silicone_Fluid Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, Simple_Green_Cleaner, '--b', label="Simple_Green_Cleaner Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(Freq, WD_40, '-g', label="WD_40 Data") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(Freq), max(Freq)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Dielectric Constant') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Dielectric Constant (e)') #add y-axis title


plt.show() #required to display plots