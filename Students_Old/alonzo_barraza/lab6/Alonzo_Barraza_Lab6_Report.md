# Lab 6 Report
Alonzo Barraza 

## Background
For Lab 6, the objective was to learn about two different types of filter. The first filter that was studied was the low-pass filter which consisted of two seperate designs that would be compared. In the first design, the low-pass filter was constructed to be a maximally flat T-Line while the second one was tapped. For the second filter, a band-stop filter was looked at and studied. Both filters were to be simulated in HFSS and then constructed physically in order to compare the results. David provided milled out filters for all three designs while the rest of the class was required to make the band-stop filter with an FR4 board and copper tape.

## Design
The procedure to design all three designs where laid out for us in the lab manual which included charts and block diagrams. The first design was the low-pass filter which had design paramters of a cut-off frequency at 2.5GHz and minimal attenuation of 10dB at 3.25GHz. Using these paramters and the chart given, it was calculated that the filter was a 5th order filter. Next, the coeffecienst for the prototype could be gathered from a table also provided in the manual. These coefficients were used for the LC ladder network. After obtaining the coefficients, Richard's Transformation was applied in order to convert the shunt capacitors into shunt open circuits and series inductors into series short circuits. The following step was to use Kuroda's identities which required mulitple sub-steps. This identity allowed the series stubs to turned into shunt stubs with the use of unit elements. Once the identities were applied, the widths of the each line could calculated. The width of lines were: 8.371mm (25ohms), 3.939mm (43ohms), 3.105mm (50ohms), 1.736mm (69ohms), 0.518mm (112ohms), and 0.068mm (181ohms). All of the lenghts were quaterwave lengths but due to the dielectric, the legnths were slighty different: 16.102mm, 16.735mm, 16.920mm 17.332mm, 17.927mm, and 18.598mm respectively. In addition to being simulated in HFSS this design, along with the LC design, was simulated in Z0lver. 

The second design for the low-pass filter was to tap the open-circuit stubs. This was done by setting the widths to a fixed value of 1mm or 89ohms. Using an equation given in class (Zo,A = (89/2)cot(2*pi*l/lambda)) the new lengths could be calculated: 8.051mm (25ohms), 8.368mm (43ohms), 8.666mm (69ohms), 8.964mm (112ohms), and 9.299mm (181ohms).     

Designing the band-stop followed simliar steps like in the low-pass design but instead replaced shunt elements with shunted LC series networks and series LC parallel networks. The widths: 3.092 (50ohms), 1.454mm (75ohms), and 0.648mm (104ohms). The lenghts were quaterwave lengths with slighty differnt values: 14.069mm, 14.507mm, and 14.847mm. 

## Procedure
During the lab portion, the band-stop filter was conctructed with a FR4 board and copper tape. In order to make the filter a 50ohm line was measured, cut, and then placed on the board. This went across the board and the stubs would come off from here. Once the 50ohm line was placed, connectors were soldered ends of the board were the copper tape was. Then the stubs were measured and cut so that they could be placed. The stubs consisted of one 50ohm stub, two 104ohm stubs, and two 75ohms stubs. Soldered had to be used in order to provide good connections. When the filter was ready, measurements were taken. S11 and S21 phases and magnitudes were gathered from the network analyzer. 

## Results and Discussion
![S11 LPF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/LPF_S11_dB.png) <br>
![S21 LPF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/LPF_S21_dB.png) <br>
![S11 BSF Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S11_Phase.png) <br>
![S11 BSF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S11_dB.png) <br>
![S21 BSF Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S21_Phase.png) <br>
![S21 BSF Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/lab6/BSF_S21_dB.png)<br>

## Conclusion
The simulations showed that the tapped T-line is  better design for the low-pass because it had an attenuation of 10dB at 3.25GHz asa compared to th eT-line which was higher than that. It could also be seen that the copper tape design gives results that in close proximity of the simulated values but it is better to mil of design. This is because milling is more precise and maintains better connections. 

## Hindsight
This lab was straight forward and problems that occured were known ahead of time, like copper tape not cooperating when soldering.

## Reflection
The most difficult part of this lab was soldering the copper tape to one another. The hot air soldering tool would move and bubble up the cape, making it hard to make a connection. Other than that, this lab was a great excerise with filters.
