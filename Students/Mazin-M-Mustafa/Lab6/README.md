# Lab 6 Report
Mazin M Mustafa 

## Background

In this lab we will desing, simulate and fabricate LPF and BSF. The design of both LPF and BSF will be obtained using insertion loss method. Microstrip implementation of the filters will be done through filter transformation. The insertion loss method is used to control the transfer function behaviour of the filter specially in the pass-band. There are two possible ways to implement the filter: Maximally flat and Equal ripple. Each techique has advantages and disadvantages. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/equations.png) <br>
fig.1 : Equations for Insertion Loss

The LPF prototypes and implementations are basically lumped elements. This gives a possibility to implement the filter using discrete components or microstrip realization ... etc


## Design

The design of LPF starts with selecting cut-off frequency and substrate parameters. By identifying the rejection required for the filter will allow us to decide the number of elements in the filter. This can be obtained from design tables. These values give us the gk for each lumped element and this will be the initial design. The next step is to apply transformations by using Richards' transformations. Then by using Kuroda identities, a practically realizable microstrip version can be obtained. The same concept can be applied for BSF by introducing inverter, this gives a BSF filter. Similar process can be done for HPF and BPF.

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

