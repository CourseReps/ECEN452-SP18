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
with open('Patch_VSWR.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq [GHz]']!="END":
			x.append(float(row['Freq [GHz]']))
			y1.append(float(row['VSWR(1) []']))

#---FILE 2---#############################################################
with open('SP_JR_Stub.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y2.append(float(row['S11 SWR(U)']))
#---FILE 3---#############################################################
with open('SP_JR_Unmatched.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y3.append(float(row['S11 SWR(U)']))


##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1


ax1.plot(x, y1, '-r', label="Simulated") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y2, '-b', label="Cu Tape Stub Matched") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y3,'-g', label="Cu Tape Unmatched")#y3 vs. x, dashed-red, add lable for legend



ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=3) #add legend at location #4 (bottom-right corner)
ax1.set_ylim(0,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Patch VSWR') #add plot title plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('VSWR') #add y-axis title

plt.show()
