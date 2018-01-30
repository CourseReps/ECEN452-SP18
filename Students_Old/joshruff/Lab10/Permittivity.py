import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10= []
y11= []
y12= []
##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Acetone.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['frequency']!="END":
			x.append(float(row['frequency'])/1e9)
			y1.append(float(row['e\'']))
#---FILE 2---#############################################################
with open('DI_water.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y2.append(float(row['e\'']))
			
#---FILE 3---#############################################################
with open('Ethylene_Glycol.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y3.append(float(row['e\'']))
#---FILE 4---#############################################################
with open('Glass_Cleaner.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y4.append(float(row['e\'']))
#---FILE 5---#############################################################
with open('Hydrocal.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y5.append(float(row['e\'']))
#---FILE 6---#############################################################
with open('Isopropyl_Alcohol.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y6.append(float(row['e\'']))
#---FILE 7---#############################################################
with open('Pine_Sol.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y7.append(float(row['e\'']))
#---FILE 8---#############################################################
with open('Silicone_Fluid.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y8.append(float(row['e\'']))
#---FILE 9---#############################################################
with open('Simple_Green_Cleaner.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y9.append(float(row['e\'']))
#---FILE 10--#############################################################
with open('WD_40.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y10.append(float(row['e\'']))
##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

ax1.plot(x, y1, '-r', label="Acetone") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y2, '-k', label="DI Water") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y3, '-b', label="Ethylene Glycol") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y4, '--g', label="Glass Cleaner") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y5, '-y', label="Hydrocal") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y6,'-g', label="Isopropyl Alcohol") #plot y3 vs. x, dashed-red, add lable for legend


ax1.plot(x, y7, '--r', label="Pine Sol") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y8, '-m', label="Silicone Fluid") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y9,'--b', label="Simple Green Cleaner") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y10,'--k', label="WD-40") #plot y3 vs. x, dashed-red, add lable for legend


ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=5) #add legend at location #4 (bottom-right corner)
#ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Measured Dielectric Constants') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('e\'') #add y-axis title

plt.show() #required to display plots
