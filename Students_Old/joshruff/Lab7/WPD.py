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
with open('Wilkinson.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq [GHz]']!="END":
			x.append(float(row['Freq [GHz]'])*1e9)
			y1.append(float(row['dB(S(1,1)) []']))
			y2.append(float(row['dB(S(2,1)) []']))
			y3.append(float(row['dB(S(2,2)) []']))
			y4.append(float(row['dB(S(3,1)) []']))
			y5.append(float(row['dB(S(3,2)) []']))
			y6.append(float(row['dB(S(3,2)) []']))

#---FILE 2---#############################################################
with open('Milled_Wilkinson.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y7.append(float(row['S11 Log Mag(dB)']))
			y8.append(float(row['S21 Log Mag(dB)']))
			y9.append(float(row['S22 Log Mag(dB)']))
			y10.append(float(row['S31 Log Mag(dB)']))
			y11.append(float(row['S32 Log Mag(dB)']))
			y12.append(float(row['S33 Log Mag(dB)']))
##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

ax1.plot(x, y1, '-r', label="S11 Simulated") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y3, '-g', label="S22 Simulated") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y6, '-b', label="S33 Simulated") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y7, ':r', label="S11 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y9, ':g', label="S22 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y12,':b', label="S33 Milled") #plot y3 vs. x, dashed-red, add lable for legend



ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
#ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Wilkinson Power Divider Reflections') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('Magnitude [dB]') #add y-axis title


#----------PLOT 2-----------################################################
plt.figure(2) #initialize plot1
ax2 = plt.subplot(111) #create axes handle for plot1

ax2.plot(x, y2, '-r', label="S21 Simulated") #plot y3 vs. x, dashed-red, add lable for legend
ax2.plot(x, y4, '-k', label="S31 Simulated") #plot y3 vs. x, dashed-red, add lable for legend

ax2.plot(x, y8, ':r', label="S21 Milled") #plot y3 vs. x, dashed-red, add lable for legend
ax2.plot(x, y10,':k', label="S31 Milled") #plot y3 vs. x, dashed-red, add lable for legend

ax2.legend(loc=3) #add legend at location #4 (bottom-right corner)

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Wilkinson Power Divider Port 31 and 21 division') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax2.set_ylabel('Magnitude [dB]') #add y-axis title

ax2.set_ylim(-10,0)#Force y axis limits if necessary



#----------PLOT 3-----------################################################
plt.figure(3) #initialize plot1
ax3 = plt.subplot(111) #create axes handle for plot1

ax3.plot(x, y5, '-c', label="S32 Simulated") #plot y2 vs. x, solid-red, add lable for legend
ax3.plot(x, y11,':c', label="S32 Milled") #plot y2 vs. x, solid-red, add lable for legend

ax3.legend(loc=4) #add legend at location #4 (bottom-right corner)

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Wilkinson Power Divider Port 23 Isolation') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax3.set_ylabel('Magnitude [dB]') #add y-axis title


plt.show() #required to display plots
