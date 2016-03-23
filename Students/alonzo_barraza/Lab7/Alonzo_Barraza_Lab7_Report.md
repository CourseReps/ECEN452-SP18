# Lab 6 Report
Alonzo Barraza 

## Background
In lab 7, there were multiple designs that were studied. Four power dividers were simulated in Z0lver and some were simulated in HFSS. The power dividers consited of a delta power divider, a splitter, a four-way splitter, and Wilkinson power divider. The only design that was constructed for this lab was the time delay shifter. These designs provide a different functionality, so this lab helps distuguishes when to use which design. 

## Design
The procedure to design all three designs where laid out for us in the lab manual which included charts and block diagrams. The first design was the low-pass filter which had design paramters of a cut-off frequency at 2.5GHz and minimal attenuation of 10dB at 3.25GHz. Using these paramters and the chart given, it was calculated that the filter was a 5th order filter. Next, the coeffecienst for the prototype could be gathered from a table also provided in the manual. These coefficients were used for the LC ladder network. After obtaining the coefficients, Richard's Transformation was applied in order to convert the shunt capacitors into shunt open circuits and series inductors into series short circuits. The following step was to use Kuroda's identities which required mulitple sub-steps. This identity allowed the series stubs to turned into shunt stubs with the use of unit elements. Once the identities were applied, the widths of the each line could calculated. The width of lines were: 8.371mm (25ohms), 3.939mm (43ohms), 3.105mm (50ohms), 1.736mm (69ohms), 0.518mm (112ohms), and 0.068mm (181ohms). All of the lenghts were quaterwave lengths but due to the dielectric, the legnths were slighty different: 16.102mm, 16.735mm, 16.920mm 17.332mm, 17.927mm, and 18.598mm respectively. In addition to being simulated in HFSS this design, along with the LC design, was simulated in Z0lver. 

The second design for the low-pass filter was to tap the open-circuit stubs. This was done by setting the widths to a fixed value of 1mm or 89ohms. Using an equation given in class (Zo,A = (89/2)cot(2*pi*l/lambda)) the new lengths could be calculated: 8.051mm (25ohms), 8.368mm (43ohms), 8.666mm (69ohms), 8.964mm (112ohms), and 9.299mm (181ohms).     

Designing the band-stop followed simliar steps like in the low-pass design but instead replaced shunt elements with shunted LC series networks and series LC parallel networks. The widths: 3.092 (50ohms), 1.454mm (75ohms), and 0.648mm (104ohms). The lenghts were quaterwave lengths with slighty differnt values: 14.069mm, 14.507mm, and 14.847mm. 

## Procedure
Similar to lab 6, this lab required to design, construct, and measure a board made with copper tape. This design was a time-delay shifter that had a 90 degree shift and 180 degree shift. Since the design is not sophistiacted enough to handle switching between the two delay paths, the designs had to be made seperately. Before adding in the delay paths, the 50ohm line (like in lab 6) was measured in order to obtain the reference angle which was -444.15 degrees. The first delay path that was calculated was the 180 degree phase delay. In order to have 180 degree phase shift, 24.138mm of line was added to an arbirtary path length. The path made a "U" shape consisting of the arbitrary line length with 14.069mm legs added to either side. There was a 1mm seperation from the 50ohm line. The copper tape pieces had to soldered together, which was rather difficult due to the hot air. This path produced a phase of -237.81 degrees. Next the solder had to taken off so that 180 degree path was disconnected form the 50ohm line. After that the 90 degree path was constructed. The additional line needed was 14.069mm, therefore adding 7.0345mm to each side. For both paths an additional 1.5mm was measured out so that the copper tape pieces would overlap. The resulting phase was -511 degrees (-481.78 degrees at times). The last measerment that was taken was the thru again but taking the coupling effect from the two delay paths. The phase came out to be -440.11 degrees, showing that the additional copper tape had an affect on the thru line.   

## Results and Discussion
![S11 LPF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/LPF_S11_dB.png) <br>
![S21 LPF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/LPF_S21_dB.png) <br>
![S11 BSF Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S11_Phase.png) <br>
![S11 BSF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S11_dB.png) <br>
![S21 BSF Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S21_Phase.png) <br>
![S21 BSF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S21_dB.png)<br>

## Conclusion
The measurement portion of this lab consisted of an unknown error that multiple groups were getting. The desired results should have been -534.14 dgrees for the 90 degree shift and -624.14 degrees for the 180 degree shift. However the result for the 90 degree was off by about 20 degrees and the 180 degree shift was less negative when it should have been more negative. It was later discover that the error was coming from lack of precision in the copper tape, the FR4 board taht was being used, and an error from the network anaylzer. The arbirtay line length, though theoretically could be of any line, had an affect. It was close to 85mm then netwrok anaylzer would have a 360 degree error. This was overcome by subratcting 360 degree in the csv file for th 180 degree S21 measurement. 

## Hindsight
This lab was straight forward and problems that occured were known ahead of time, like copper tape not cooperating when soldering.

## Reflection
The most difficult part of this lab was soldering the copper tape to one another. The hot air soldering tool would move and bubble up the cape, making it hard to make a connection. Other than that, this lab was a great excerise with filters.
