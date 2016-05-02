# Lab 6 Report
Lisa Smith

## Background
The maximally flat low pass filter is a filter that only takes frequencies that are higher than the cut off frequency. By transforming the values of the capacitors and inductors to impedances, the filter can be made out of open circuit stubs. The Tapered Maximally-Flat Low-Pass Filter is another way to design the above filter with a similar response. The main difference is that all of the stubs have the same impedance and the length is changed to get the desired response. The band pass filter is used to attenuate frequencies in a certain range around a selected center frequency. 

## Design
For the maximally flat low pass filter:

The values for each impedance of the stubs and connecting transmission lines are given. Each has a length of 1/8 the effective wavelength at 2.5 GHz. The widths of each were then found using an online calculator. The chart below shows the values used for simulation.

![lab_6_values1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_values1.PNG)
 
For the tapered maximally-flat low-pass filter:

The values for each impedance of the stubs and connecting transmission lines are given. Each has a length found using the equation below at 2.5 GHz. The widths of each were then found using an online calculator. The chart below shows the values used for simulation.

![lab_6_eq](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_eq.PNG)

![lab_6_values2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_values2.PNG)

For the band stop filter:

The values for each impedance of the stubs and connecting transmission lines are given. Each has a length of 1/4 the effective wavelength at 3 GHz. The widths of each were then found using an online calculator. The chart below shows the values used for simulation.

![lab_6_values3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_values3.PNG)
 
Each of these designs were made using the given HFSS files and substituting the calculated values above.

## Procedure
In lab, the maximally flat low pass filter was premade and measured using the network analyzer. The band stop filter was designed using the same design dimensions used for simulation. First a single 50 Ohm transmission line was created on the 62 mil FR4 substrate. This was then measured using the network analyzer. The stubs were then added and soldered to the existing 50 Ohm line. This was measured and the results are shown below.

## Results and Discussion
The simulated and measured results line up fairly well for the maximally flat low pass filter. There is a major difference in the S11 parameter form about 2.5 GHz to 3.5 GHz. This dip in the S11 parameter of the measured result is unusual, however, it does not affect the filter’s performance.

![lab_6_graph1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_graph1.PNG)

The tapered maximally-flat low-pass filter was not created and only the simulated results are shown below. The results do show the filter blocking frequencies above 2.5 GHz, as desired in the design.

![lab_6_graph2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_graph2.PNG)

The design operated similarly to the simulated design. Because the device was created by hand, there is some error in both the widths and lengths of the lines in the filter. Here, the stubs were cut too short and therefore the device works at a slightly higher frequency than desired. 

![lab_6_graph3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_graph3.PNG)

![lab_6_graph4](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-6/lab_6_graph4.PNG)

## Conclusion
In this lab, both types of filter were simulated in HFSS and had similar results to the premade maximally flat low pass filter and the constructed band stop filter. Because the measured devices did not have the exact same design dimensions as the simulated models, there are some discrepancies in the results.

## Hindsight
The major problem with constructing the filter was the accuracy in cutting out the lengths and widths of the transmission lines. Copper tape is not forgiving if the dimensions are cut slightly wrong. Also cutting straight lines is difficult.

## Reflection
This lab did give good insight to the operation of different types of filters and a couple different ways to construct them and the advantages to each type of design.
