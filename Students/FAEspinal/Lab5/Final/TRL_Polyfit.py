import matplotlib.pyplot as plt
import numpy as np
import csv

f0 = 3e9  #center frequency
phase = 90.6382 #S21 phase of deembedded Line at center frequency
line_length = 13.9e-3 #additional Line length (physical length)

eeff = (3e8*phase/(f0*line_length*360))**2 #effective dielectric constant
vp = 3e8/np.sqrt(eeff) #phase velocity
delay = line_length/vp #delay of additional Line length
delay = delay/1e-12 #convert to pico seconds
print('delay = ', delay, 'ps')

f = []
X = []

with open('Reflect_im_Z.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f.append(float(row['Freq [GHz]']))
        X.append(float(row['im(Z(1,1)) []']))

f = np.array(f)
X = np.array(X)

f = f*1e9 #convert GHz to Hz
C = -1/(2*np.pi*f*X) #convert reactance to capacitance

p3 = np.polyfit(f, C, 3) #get 3rd order polynomial coefficients
p = np.poly1d(p3) #create function based on polynomial

#print coefficients
print('C0 = ',p3[3]/1e-15)
print('C1 = ',p3[2]/1e-27)
print('C2 = ',p3[1]/1e-36)
print('C3 = ',p3[0]/1e-45)

plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(f, C, '-b') #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f, p(f), '-r') #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(f), max(f)) #set x-axis limits
plt.title('TRL Capacitance') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Capacitance [F]') #add y-axis title

plt.show() #required to display plots
