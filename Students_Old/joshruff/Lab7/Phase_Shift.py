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
with open('MM_JR_THRU.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq(Hz)']!="END":
			x.append(float(row['Freq(Hz)']))
			y1.append(float(row['S11 Phase']))
			y2.append(float(row['S21 Phase']))



#---FILE 2---#############################################################
with open('MM_JR_90deg.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq(Hz)']!="END":
			y3.append(float(row['S11 Phase']))
			y4.append(float(row['S21 Phase']))

#---FILE 2---#############################################################
with open('MM_JR_180deg.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq(Hz)']=="END":
			break
		y5.append(float(row['S11 Phase']))
		y6.append(float(row['S21 Phase']))




##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

#ax1.plot(x, y1, '-r', label="S11 THRU") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y2, '-r', label="S21 THRU") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y3, '-b', label="S11 90Deg ") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y4, '-g', label="S21 90Deg") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y5, ':g', label="S11 180Deg") #plot y2 vs. x, solid-red, add lable for legend

ax1.plot(x, y6, '-b', label="S21 180Deg")#plot y2 vs. x, solid-red, add lable for legend


ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
#ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Phase SHifter S21 Measurement') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('Magnitude [dB]') #add y-axis title


plt.show() #required to display plots
