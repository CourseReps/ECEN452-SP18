import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
e_Acetone = []
e_DI_water = []
e_Ethylene_Glycol = []
e_Hydrocal = []
e_Isopropyl_Acohol = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Dielectric_Const_Plot.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['frequency']))
        e_Acetone.append(float(row['e_Pine_Sol']))
        e_DI_water.append(float(row['e_Silicone_Fluid']))
        e_Ethylene_Glycol.append(float(row['e_Simple_Green_Cleaner']))
        e_Hydrocal.append(float(row['e_WD_40']))
        e_Isopropyl_Acohol.append(float(row['e_Glass_Cleaner']))


##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f1, e_Acetone, '-b', label="eps_r_Pine_Sol") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, e_DI_water, '-r', label="eps_r_Silicone_Fluid") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, e_Ethylene_Glycol, '-g', label="eps_r_Simple_Green_Cleaner") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, e_Hydrocal, '-k', label="eps_r_WD_40") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, e_Isopropyl_Acohol, '-c', label="eps_r_Glass_Cleaner") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Dielectric Constant') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Dielectic Constant') #add y-axis title

plt.show() #required to display plots