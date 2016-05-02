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
with open('Milled_Hybrid_S11.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq(Hz)']!="END":
			x.append(float(row['Freq(Hz)'])/1e9)
			y1.append(float(row['S11 Log Mag(dB)']))

#---FILE 2---#############################################################
with open('Milled_Hybrid_S21.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y2.append(float(row['S21 Log Mag(dB)']))
			y10.append(float(row['S21 Phase()']))
#---FILE 3---#############################################################
with open('Milled_Hybrid_S31.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y3.append(float(row['S21 Log Mag(dB)']))
			y11.append(float(row['S21 Phase()']))

#---FILE 4---#############################################################
with open('Milled_Hybrid_S41.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq(Hz)']!="END":
			y4.append(float(row['S21 Log Mag(dB)']))
#---FILE 5---#############################################################
with open('Lab8-Hybrid-Input-dB.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq [GHz]']!="END":
			y5.append(float(row['dB(S(1,1)) []']))
			y6.append(float(row['dB(S(2,1)) []']))
			y7.append(float(row['dB(S(3,1)) []']))
			y8.append(float(row['dB(S(4,1)) []']))


#---FILE 6---#############################################################
with open('Lab8-Hybrid-Input-Phase.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Freq [GHz]']!="END":
			y9.append(float(row['cang_deg(S(2,1))-cang_deg(S(3,1)) [deg]']))
for i in range(0,len(x)-1) :
	y11[i]=y10[i]-y11[i]

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1

ax1.plot(x, y5, '-r', label="S11 Simulated") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y6, '-b', label="S21 Simulated") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y7, '-g', label="S31 Simulated") #plot y3 vs. x, dashed-red, add lable for legend
ax1.plot(x, y8, '-m', label="S41 Simulated") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y1, '--r', label="S11 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y2, '--b', label="S21 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(x, y3,'--g', label="S31 Milled") #plot y3 vs. x, dashed-red, add lable for legend

ax1.plot(x, y4,'--m', label="S41 Milled") #plot y3 vs. x, dashed-red, add lable for legend


ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
#ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Hybrid Coupler S-Parameters') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax1.set_ylabel('Magnitude [dB]') #add y-axis title


#----------PLOT 2-----------################################################
plt.figure(2) #initialize plot1
ax2 = plt.subplot(111) #create axes handle for plot1

ax2.plot(x, y9, '-b', label="Simulated") #plot y3 vs. x, dashed-red, add lable for legend
ax2.plot(x, y11, '-r', label="Milled") #plot y2 vs. x, dashed-red, add lable for legend


ax2.legend(loc=3) #add legend at location #4 (bottom-right corner)

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Hybrid S21-S31 Phase Difference') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
ax2.set_ylabel('Phase [degrees]') #add y-axis title
ax2.set_ylim(0,200)#Force y axis limits if necessary

plt.show() #required to display plots
