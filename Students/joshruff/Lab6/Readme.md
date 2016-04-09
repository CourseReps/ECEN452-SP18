# Lab 6 Report
Joshua Ruff

## Background
This lab consisted of three separate devices. The first was a Maximally Flat Butterworth Low Pass Filter which was designed based off of an LC Ladder Network. The LC network was transformed into a transmission line equivalent using Richard's Transformation. Kuroda's Identities were then used to transform series stubs to shunt stubs. 

For the second device this low pass filter was transformed into a tapped stub equivalent. This allowed for the filter to be put into a more compact space. 

The third device was an equiripple band stop filter. This filter was designed using solely quarter-wave sections of line for the subs and unit elements. 

## Design

###Low Pass Filter
The Low Pass Filter was designed for a cut-off frequency of 2.5 GHz and a minimum attenuation of 10 dB by 3.25 GHz. 

![Order](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Order_Select.png)<br>

The result was plotted on the following Graph: 

![Filter_Order](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Filter_Order.PNG)

The Order chosen on the graph will determine the number of capacitors and inductors in the prototype ladder network. Because a 5th order filter is desired, the ladder network consists of five elements: three capacitors, and two inductors.

![MaxFlat_Ladder](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/MaxFlat_Ladder.png)

The normalized values for these circuit elements were taken from the following Butterworth Filter Prototype table. 

![MaxFlat_Table](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/MaxFlat_Table.png)

Richard's Transformations were then used to transform the ladder network into a Transmission Line equivalent. Richard's Transformations involve replacing capacitors and inductors with eight-wave open circuit and short circuit stubs respectively. The stubs will have a characteristic impedance based on the value of the capacitor or inductor which said stub is replacing: 

![Richard's_Transformation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Richard_Trans.png)

Following this step, Kuroda's Identities were used to  transform the series stubs into shunt stubs which can actually be implemented in a transmission line. Kuroda's identities also allow for stubs to be physically separated from one another, which is useful to minimize coupling between them. 

![Kuroda_Identity](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Kuroda_Identity.png) 
(Source: http://course.ee.ust.hk/elec344/lect31.pdf)

Once the stubs are separated, the Impedances ase scaled by the impedance of the feed line (50 Ohms), and the widths of the microstrip line for FR-4 Substrate are calculated. The resulting device is pictured below: 

![LPF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/LPF_T-Line.PNG)

### Tapped Stub Low Pass Filter

This Low pass filter could be converted into a tapped stub filter by converting the stubs in the current filter to two parallel stubs with the same input impedance. This transformation involves converting the stubs into 89 Ohm stubs (so they all have the same width) with varying length. The length is calculated by the relation: 

![Tapped_Eq](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Tapped_Stub-eq.png)

Where ZoA is the original stub's impedance, ZoB is 89 Ohms, and L is the length of the parallel stubs. Like in the previous filter, the stubs are separated by eighth wave unit elements of either 69 or 112 Ohms. The final device is pictured below: 

![Tapped_Stub_LPF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/LPF-Tapped_Stub.PNG)
https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Kuroda_Identity.png)

###Equi-Ripple Bandstop Filter
The development of an equi-ripple filter begins the same way as the development of the Maximally Flat filter did. A ladder network of Inductors and Capacitors is constructed based on a table of known values. This low pass prototype is then converted to a band pass prototype by replacing each series inductor or shunt capacitor in the circuit with a series or paralell LC network. Quarter wave resonators were used to replace the LC networks so that each LC network could either be converted into a quarter-wave stub separated by a quarter wave transformer. For band stop characteristics, all lengths are quarter-wave and all stubs are open circuit. The scaled impedance values of each stub were calculated by the relation:

![BP_Stub](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/BP_Stub.png)

With the impedances and electrical lengths determined, the physical lengths and widths were calculated via a microstrip line width calculator. The resulting device is pictured below: 

![Equi-Ripple](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/Equi-Ripple.PNG)


## Procedure
Each device was modeled and simulated in HFSS. Also, David milled a version of each device, which was tested with the Network Analyzer. The Network Analyzer was configured for a 15mm reference plane to calculate out the effects of the connectors and isolate the filter response. In Lab the Equi-Ripple Band Stop Filter was constructed on FR4 substrate using copper tape as the conductor. A heat gun was used to solder the lengths of tape to one another as well as to solder connections to the boards. The results of each of these filters are plotted in the following section.

## Results and Discussion
(analysis coming)
###Low Pass Filter
![LPF_TLine](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/LPF_TL-SParams.png)

###Tapped Stub Filter
![LPF-TappedStub](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/LPF-TappedStub-SParam.PNG)

###Equi-Ripple Bandstop Filter

![BSF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab6/Pictures/BSFilter.png)

## Conclusion
The filters designed in this lab achieved the desired behavior (i.e the low-pass filter exhibited low-pass filter behavior, and the band-stop filter exhibited band-stop filter behavior); however, there were discrepancies in the cut-off frequency of the low pass filters and the band-stop filters. The frequency range didn't necessarily match up to the desired range, likely due to small errors in calculations. 

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
