# Lab 6 Report
Benjamin Jack

## Background
The maximally flat lowpass filter (Butterworth filter) is designed to be as flat as possible over the passband and
then to reject frequencies outside the passband. The maximally flat portion is important so the filter not only
rejects appropriate frequencies, but also treats all desired passband frequencies the same.(1) The tapped filter
design allows us to use, potentially, less space on the substrate and more importantly allows us to use higher
impedance, narrower, stubs which do not couple with one another on the substrate. The 5th order .5dB equi ripple
band stop filter is used to stop only a set of frequencies in a band and allow all other frequencies to pass through.
The higher the order of the filter, the more precise the filter cutoffs will be, but fifth order is just arbitrary here.
The .5dB means the oscillations in the passband are under .5dB in magnitude. Equiripple means the filter has 
equal ripple in both the pass and stop bands.(2)

## Design
*Task 1:<br>
Data:
Zo = 50 ohms, 62 mil thick = 1.578mm, FR4 (Er = 4.1), f[1,5] GHz, 15mm ref. plane

In task one, we designed a maximally flat low pass filter(Butterworth filter) with cutoff frequency fc = 2.5GHz and a
minimum attenuation of 10 dB at 3.25GHz. I used the graph below relating the cutoff frequency and attenuation at a
set frequency to calculate the order of the filter required, which is a fifth order filter.

Figure 1: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/FilterOrder.PNG)<br>

I then used a lookup table to determine the filter coefficients for a fifth order Butterworth low pass filter
prototype. g1=.618, g2=1.618, g3=2.00, g4=1.618, g5=.618 The ladder network is shown in Figure 2.

Figure 2: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/Ladder.PNG)<br>

In the diagram, we see three shunt capacitors and two series inductors. We can use Richard's Transformations to 
conver the capacitors to open circuit stubs and the inductors into short circuit stubs. 
For (shunt) capacitors: z = 1/g. For (series) inductors: z = g. We get z1=1.618, z2=1.618, z3 =.5, z4=1.618, z5=1.618
Now that we have a series of stubs, we can us Kuroda's identities to conver the stubs into all open circuit stubs
by inserting unit elements at the ends of the circuit and transforming the elements in toward the middle of the
circuit. We can use symmetry here to only have to work from one side of the circuit. First we can insert a unit
element with ue=1. By Kuroda's identities, we know N1=1+ue/z1. Here N1 is 2.613. We flip the unit element and OC
shunt element order in the circuit and we now have a SC element followed by a unit element with a new values:
z1'=ue1/N1=.382 and ue1'=z1/N1=.619. We now add a second unit element to the series so we have: unit element,series SC,
unit element, and another series SC. As we can now see, one more transformation each gives us all OC stubs. We calculate:
N2=1+z1'/ue2=3.618, N1'=1+z2/ue1'=1.382. Now we calculate new shunt and unit element values of:z1''=ue2*N2=3.618,
ue2=z1'*N2=1.382, z2'=ue1'*N1'=.854, ue1''=2.236.
The final result, after impedance scaling where we multiply by our characteristic impedance of 50 ohms,
is given by the circuit below:

Maximally Flat LPF T-Line Model:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/Final1.PNG)<br>

Using the online microstrip calculator, we found the wavelength and line width for each of the 1/8 wavelength sections.
For the lumped element model which we found with the ladder network and the lookup table, we can find the value of
the capacitors and inductors by performing impedance and frequency scaling:L=(Zo*g)/w and C=g/(Zo*w).
We get:C1=.787pF, L2=5.15nH, C3=2.55pF, L4=5.15nH, C5=.787pF.

For the center-tapped stub, we can use our knowledge of OC stub impedances and parallel circuit elements to calculate
the values for the stub lengths given an 89 ohm (1mm wide) stub. We know Zoc = j*Zo*cot(B*l). Combining two of these
OC elements in parallel, we get the impedance as -jZo*cot(B*l)/2. This impedance is equal to the impedance we calculated
for the T-line model of our LPF and Zo in this equation is 89 ohms. If we substitute B = 2pi/lambda and l = X*lambda,
we can solve for X for each stub. X = arccot(2*ZocA/ZocB)/(2pi) where ZocA is the T-line impedance and ZocB is 89 i=ohms.
We get X1=.038 = X5, X2 = .1277 = X4, X3 = .169. By the microstrip calculator, we know the wavelength at 2.5GHz through an
89 ohm line is 70.6mm so we have line lengths:l1=l5=2.68mm, l2=l4=9.02mm, l3=11.90mm.

*Task 2:

*Data:
fc=3GHz, delta(d)=.5, Zo=50, FR4(Er=4.1), t = 62mil(1.578mm), f[2.25,3.75] GHz

First, I used a lookup table to determine the constants for a fifth order .5dB equiripple band stop filter given by:
g1=g5=1.706, g2=g4=1.23, g3=2.54, g6=1. Similar to the LPF design, we assemble the same LPF ladder network prototype.
From here, however, we covert the shunt capacitors to a shunt 'series LC' and a series inductor to a series 'parallel LC'.
In the same method, but using quarter wavelength sections, we can transform away series components until we have only
shunt OC stubs separated by quarter wavelength unit elements. However, because we are maintaining a T-line model, we
can continue to solve the circuit through instead of solving for the L and C element values and the following formula 
drops out: Z = (4Zo)/(pi*d*g), which we can use to solve for each impedance for the OC stubs and each unit element is
defined by our characteristic impedance of 50 ohms. The final result is seen below.

BSF Final Values:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSFFinal.PNG)<br>

I did not have to make any modifications for either design while in lab other than redoing my incompetent soldering.

## Procedure
In lab, we took the clean FR4 sheets and first cut out a 50 ohm transmission line for 2.5GHz, then we cut out stubs
using copper tape which were the appropriate width and length using the microstrip calculator and the results given
to us in the image above: "Maximally Flat LPF T-Line Model". Then, we hooked up the filter and collected the data from
the VNA. The results are shown below. We did not implement the center-tapped stub model in lab. For the BSF, we did
the exact same thing as with the LPF and the results are once again below.

## Results and Discussion
LPF T-Line Mag: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/LPF_TLine_dB.png)<br>
From this plot, we can see that at our cutoff frequency of 2.5GHz our circuit is not attenuating the signal and does
not until 3.5GHz. This occurs because of the coupling between the stubs, in particular where the 25 ohm stub is so wide
and so close to the stubs next to it. The S11 magnitude is low until the circuit reaches its cutoff and reflects the signal.

LPF T-Line Phase: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/LPF_TLine_phase.png)<br>
The phase measurements are approximately correct for the S21 parameter but are not de embedded to exactly align at
the same frequencies and there are still coupling effects in the higher frequencies of the measured data.

LPF Tapped T-Line Mag: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/LPF_Tapped_dB.png)<br>
The magnitude plot here shows how the center-tapped stub model eliminates our coupling effects and we get a clean
cutoff at 2.5GHz with -10dB at 3GHz. Once again, S11 is attenuated in the passband.

LPF Tapped T-Line phase: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/LPF_Tapped_phase.png)<br>

BSF S11 Mag: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSF_S11_Mag.png)<br>
The S11 magnitude exhibits almost the inverse relationship to the S21 magnitude as the signal is reflected back to
the port.

BSF S21 Mag: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSF_S21_Mag.png)<br>
From the magnitude of S21, we see there were definitely some problems with our tape filter. The center frequency was
around 3.5 GHz instead of 3GHz and our equiripple did not approach 0db, in the bandpass region. This could have been
from a number of problems: our measuring and cutting, the distances separating stubs, the length of stubs and our soldering.
I think the biggest problem is when we had to resolder several times, our tape started to peel off the substrate
and change the output significantly. The HFSS shows the nice ideal behavior across the bandstop region as the signal is
attenuated from 2.25-3.75 GHz and the signal passes through outside of the stopband.

BSF S11 Phase: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSF_S11_Phase.png)<br>

BSF S21 Phase: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSF_S21_Phase.png)<br>
The phase measurements seem to align reasonably well other than being shifted off a small amount. There are steep
slopes wherever the gain changes rapidly.

BSF Total Mag: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSF_Mag.png)<br>

BSF Total Phase: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab6/BSF_Phase.png)<br>
A lot of the phase results seemed to be off because we were not particularly interested in the phase measurements so we
did not worry about de-embedding.

## Conclusion
The main points of the LPF design were the simple design process using a low pass prototype and filter table and
graphs to get the desired response with minimal resources and then knowing how to manipulate the prototype to get
a practical solution. Here, we used Kuroda's identities, Richard's transformations, impedance and frequency scaling, and 
finally center-tapped stubs, to come up with a simple filter design which can be implemented practically on FR4
substrate in microstrip without any series stubs in particular. For the band stop filter, it is important to realize how
the same set of manipulations can be used to design a different filter. It is also important to see how we can choose
the width of the band stop filter. I did not have any trouble with the design after I understood the theory behind it
as it was simply plugging in numbers.

## Hindsight
I wish I knew how to solder better than I do. I also wish I had remembered the open circuit impedance because it
was really simple and I just forgot what it was for a while.

## Reflection
The most challenging part of this lab was the theory behind the transformations, in particular, understanding the
derivations which were not given in the lab manual. However, the textbook was very helpful and the actual theory
is not very mathmatically complex, it just takes some choice manipulation.

## Citations
(1) https://en.wikipedia.org/wiki/Butterworth_filter
(2) http://www.bores.com/courses/intro/filters/4_equi.htm
