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
y13= []
y14= []
y15= []
y16= []
##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Design2_0.0V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq(Hz)']!="END":
			x.append(float(row['Freq(Hz)'])/1e9)
			y1.append(float(row['S21 Log Mag(dB)']))
			y9.append(float(row['S21 Phase']))
#---FILE 2---#############################################################
with open('Design2_0.1V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y2.append(float(row['S21 Log Mag(dB)']))
			y10.append(float(row['S21 Phase']))
#---FILE 3---#############################################################
with open('Design2_0.5V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y3.append(float(row['S21 Log Mag(dB)']))
			y11.append(float(row['S21 Phase']))

#---FILE 4---#############################################################
with open('Design2_1.0V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y4.append(float(row['S21 Log Mag(dB)']))
			y12.append(float(row['S21 Phase']))
#---FILE 5---#############################################################
with open('Design2_2.0V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y5.append(float(row['S21 Log Mag(dB)']))
			y13.append(float(row['S21 Phase']))
#---FILE 6---#############################################################
with open('Design2_3.0V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y6.append(float(row['S21 Log Mag(dB)']))
			y14.append(float(row['S21 Phase']))
#---FILE 7---#############################################################
with open('Design2_4.0V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y7.append(float(row['S21 Log Mag(dB)']))
			y15.append(float(row['S21 Phase']))
#---FILE 8---#############################################################
with open('Design2_5.0V.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y8.append(float(row['S21 Log Mag(dB)']))
			y16.append(float(row['S21 Phase']))


##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

ax1.plot(x, y1, '-r', label="0.0 V") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y2, '-b', label="0.1 V") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y3, '-g', label="0.5 V") #plot y3 vs. x, dashed-red, add lable for legend
ax1.plot(x, y4, '-b', label="1.0 V") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y5, '-g', label="2.0 V") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y6, '-m', label="3.0 V") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y7,'-c', label="4.0 V") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y8,'-k', label="5.0 V") #plot y3 vs. x, dashed-red, add lable for legend


ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
#ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Graduate Design 2 S21 Magnitude vs Frequency') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('Magnitude [dB]') #add y-axis title



##Plotting
plt.figure(2) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

ax1.plot(x, y9, '-r', label="0.0 V") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y2, '-b', label="0.1 V") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y3, '-g', label="0.5 V") #plot y3 vs. x, dashed-red, add lable for legend
ax1.plot(x, y12, '-b', label="1.0 V") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y13, '-g', label="2.0 V") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y14,'-m', label="3.0 V") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y15,'-c', label="4.0 V") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y16,'-k', label="5.0 V") #plot y3 vs. x, dashed-red, add lable for legend

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
#ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Graduate Design 2 S21 Phase vs Frequency') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('Phase [degrees]') #add y-axis title


plt.show()
