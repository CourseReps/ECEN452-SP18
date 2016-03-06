# Lab 5 Report
Mazin M Mustafa 

## Background

TRL: 

TRL calibration is a very useful calibration technique. TRL allows us to move the reference planes into the test fixture. This

is important in order to cancel the effect of the transmission lines and coaxial connectors.

RF PIN Diode switch:

The second part is about PIN diode switch design. The purpose of this circuit is to design an RF switch controlled by DC bias.

The key point in this design is to isolate the RF circuit from the DC circuit using a bias T. This simply achieved by

introducing a high impedance quarter wave-length stub that can produce an open-circuit for RF signal. For the DC signal the

circuit will be a short circuit, but also open-circuit from the RF transmission line because because of blocking capacitors.

## Design

TRL:

The calibration kit design for 50 ohm transmission line. The calculations for 50 ohm microstrip is based on the follwoing

parameters:

Z0 = 50 ohm

h = 62 mil FR4

Dielectric constant = 4.1

tand = 0.01

fL = 1 GHz

fH = 5 GHz

Refrence plane = 15 mm

fo = (fL+fH)/2 = 3 GHz

Using microstrio equations : 

w = 3.175 mm 

Effective dielectric constant = 3.14

Quarter wave-length = 11.36 mm 

Based on the discussion in lab 3, the dimension of Line = 41.36 mm. The dimesnion of Thru = 30 mm. The dimension of Refl = 15

mm.

The Line dimension was optimzed to 44.1 mm and w to 3.18 mm

The circuit diagram:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/TRL2.png) <br>

RF PIN Diode switch:

The frequency of this design is fo = 2.5 GHz. 

for Z0 = 50 ohm

w = 3.175 mm

Effective dielectric constant = 3.14

Quarter wave-length = 16.94 mm

for Z0 = 100 ohm

w = 3.175 mm

Effective dielectric constant = 3.14

Quarter wave-length = 17.71 mm optimized to 17.6 mm

The circuit diagram: Source David M. Pozar 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Circuit.png) <br>

## Procedure

TRL:

1- Frequncy of design was calculated

2- The 50 ohm microstrip dimesnions were calculated

3- Design models were simulated using HFSS

4- De-embding was applied to the excitation ports

5- Design was optimzed to achieve almost ideal results

6- Results were obtained and compared to measured results

7- Polynomial coeffiecients were calculated for the Refl capacitance

RF PIN Diode swistch:

1- Microstrip lines for 50 and 100 ohms weree calculated

2- Quarter wave-length transmission lines for short-circuit stub and short-circuit bias stube were calculated

3- The complete design of RF PIN Diode siwitch was simulated and optimized

4- Results were obtained and compared to the measured results

## Results and Discussion

TRL results:

S21 for Line:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Line_S21_dB.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Line_S21_phase.png>) <br>

S21 for Thru:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Thru_S21_dB.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Line_S21_phase.png) <br>

Refl capacitance:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Capacitance.png) <br>

Polynomial coefficients:

C0 = -8.999

C1 = 76341.87

C2 = -19366.39

C3 = 1591.59

RF PIN Diode switch results:

OFF S11 & S21

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/OFF.png) <br>

ON S11 & S21

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/ON.png) <br>

## Conclusion

HFSS & measured results were almost identical for the TRL calibration kit. The HFSS & measured results for RF PIN Diode switch

were very close but not identical. This is due to the modeling of the Diode in HFSS. From the results obtained for both TRL

calibration kit and RF PIN Diode switch, one can conclude that both designs were successfully obtained.

## Hindsight

It would be better to fabricate the TRL designs and go throught the calibration procedure. 

## Reflection

Optimizing the HFSS design took most of the time.
