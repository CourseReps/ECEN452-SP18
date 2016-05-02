#Permeability Measurements

import matplotlib.pyplot as plt
import numpy as np
import math as mmm
import cmath as ph

#Initialize arrays for x - Freq(Hz), y - Mag(dB), z- Phase(deg)
#The voltage range is from 1 to 5 volts

V = np.arange(0,5.01,.01)
#The capacitance range is from ... to ... unknown at the moment, we don't know the relationship
#between the voltage and capacitance
#C = []
#For now we are using a variable imaginary impedance until we know what sort of capacitor and inductor
#values we will have.
#X = []
#Range of inductors if we choose to use it
#L = []

#SMV 1247
#1-9 pF

#Z01 and Z02 are switched...

#360 degrees phase shift
#HFSS Model
#Loss




L = 3e-6#Inductance of lumped inductor or stub
w = 2*mmm.pi*2.45e9#Range of frequencies 

###QWT Values
Z01 = 10 #Lower than Z02 ###Second Quarter-Wave Transformer
Z02 = 100###First Quarter Wave Transformer
#10 pF constant



###VARACTOR PARAMETERS 
C = (.0084*V**4-.194*V**3+1.6403*V**2-6.032*V+8.8594)*1e-12#Polyfit Varactor capacitance
Ls = 1.5*1e-9
Cp = .54*1e-12
Rs = 4.9







###Intermediate arrays used to solve for input impedance
X = []#Impedance of veractor diode model and inductor/stub
ZinPrime = []
Zin = []
ZPar = []
out = []
final = []
mag = []
maggg = []
refl = []
for i in range (0,501):
    X.append(complex(0, w*(Ls+L))+1/(complex(0,w*Cp)+1/complex(Rs,(-1/(w*C[i])))))

for j in range (0,501):
    ZinPrime.append(Z01*Z01/X[j])

for k in range (0,501):
    ZPar.append(ZinPrime[k]*X[k]/(ZinPrime[k]+X[k]))

for l in range (0,501):
    Zin.append(Z02*Z02/ZPar[l])

for x in range (0,501):
    refl.append((Zin[x]-50)/(50+Zin[x]))

for m in range (0,501):
    #out.append(ph.phase(Zin[m]))
    out.append(ph.phase(refl[m]))
# for n in range (0,401):
#     if final[n] < -mmm.pi:
#         final[n] = final[n]+2*mmm.pi

for n in range (0,501):
    final.append(180*out[n]/mmm.pi)

for n in range (0,501):
    mag.append(abs(refl[n]))





#print min(mag)
#print max(mag)




#Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(V, final, '-b', label="Phase") #plot y vs. x, solid-blue, add lable for legend

ax1.set_xlim(min(V), max(V)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Phase vs V') #add plot title
plt.xlabel('Voltage (V)') #add x-axis title
plt.ylabel('Phase (deg)') #add y-axis title

plt.figure(2) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(V, mag, '-r', label="Mag") #plot y vs. x, solid-blue, add lable for legend
ax1.set_xlim(min(V), max(V)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Magnitude ') #add plot title
plt.xlabel('Voltage (V)') #add x-axis title
plt.ylabel('Magnitude ') #add y-axis title

plt.show()
