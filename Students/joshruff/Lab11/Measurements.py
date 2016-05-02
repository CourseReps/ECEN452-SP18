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
with open('Air.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['frequency']!="END":
			x.append(float(row['frequency'])/1e9)
			y1.append(float(row['e\'']))

#---FILE 2---#############################################################
with open('Cardboard.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y2.append(float(row['e\'']))

#---FILE 3---#############################################################
with open('Plexiglass.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['frequency']!="END":
			y3.append(float(row['e\'']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

ax1.plot(x, y1, '-r', label="Air") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y2, '-g', label="Cardboard") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y3, '-b', label="Plexiglass") #plot y3 vs. x, dashed-red, add lable for legend

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=1) #add legend at location #4 (bottom-right corner)
ax1.set_ylim(0,6)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Relative Permittity Measurements') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('Relative Permittivity') #add y-axis title

plt.show() #required to display plots
