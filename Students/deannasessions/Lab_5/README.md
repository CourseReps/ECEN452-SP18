# Lab 5 Report
Deanna Sessions

## Background
This lab involves two devices that were simulated as well as created and tested. First, a Thru-Reflect-Line (TRL) calibration kit was designed to work over 1GHz to 5GHz centering at 3GHz. This device was then fabricated and data was taken using the Network Analyzer. The device was also created in HFSS and then simulated to check the accuracy of the fabrication. Second, a PIN diode switch containing two short circuit choke lines was designed and fabricated to be tested in both the "ON" and the "OFF" stages. This PIN diode switch was also created in HFSS to be simulated for comparison. All data was then graphed using a Python script.

## Design
Design parameters to be taken into consideration:
Zo = 50ohms
h = 62 mil
FR4 substrate
Freq range = 1GHz - 5GHz
Solution freq = 3 GHz

TRL kit: An online microstrip calculator was used to determine the width of the 50ohm transmission line (approximately 3.09mm) and the length of the quarter wavelength that is added to the Line standard (approximately 14.07mm). This resulted in a design with T = 30mm, R = 15mm, and L = 44.07mm all of which having a w = 3.09mm. This design had a decent result, but it wasn't as perfect as expected with regard to phase when it was simulated. This required a bit of tweaking and I never did get it quite right within the design, but the results I was getting appeared to have too high of an impedance so I increased the width of the line in the hopes of dropping the impedance to obtain better matching. The main issue came from the phase of the thru line where I was able to get a decent response in the simulation, but not as precise as I had hoped for.

PIN Diode Switch: The online microstrip calculator was once again used to determine the width of the 50ohm transmission line at a center frequency of 2.5GHz (approximately 3.1mm) and the width of the 100ohm choke lines (approximately 0.723mm). Using the online calculator we were able to obtain the effective wavelength necessary to calculate the lengths of the 100ohm choke lines. These 100ohm lines are each a quarter of the effective wavelength (17.8mm). These were once again simulated and required a bit of tweaking within HFSS to lower the impedance of the 50ohm lines by increasing the width to 3.2mm and increasing the stub lengths to 18.1mm. 

Both designs were simulated in HFSS and the data was compared to measured data taken in lab. 

## Procedure
TRL Kit: We calculated the necessary lengths and widths of each part of the calibration and input those values into HFSS to test the response. These were then tweaked based on the response in an attempt to gain a more precise calibration kit. David fabricated the TRL kit using the milling machine to be tested using the vector network analyzer (VNA). The VNA was placed in calibration mode and each portion of the TRL kit was tested. The reflect was attached to Port 1 to measure an S11 response and then placed on Port 2 to measure an S22 response. The Thru and Line were then attached to both 1 and 2 ports for S11, S21, S12, S21 responses. These responses were recorded in a .csv file to be analyzed and compared to the simulated data.

PIN Diode Switch: This was fabricated and tested for response using the VNA much like the TRL kit was tested. This switch was tested in both "ON" and "OFF" modes. 

## Results and Discussion
Below are the results from Lab 5 and the analysis of each plot:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/S21_Line_Measured.png)<br>

This image is the S21 response of the Line portion of the TRL kit and it can be seen that the simulated result is obviously smoother than the measured response, but if the scale of the y-axis is taken into account, the plots can be considered within the realm of error that fabrication and free space testing would provide in terms of noise.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/S21_Line_Phase.png)<br>

The S21 Line Phase response was almost identical for measured and simulated.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/S21_Thru_Magnitude.png)<br>

The S21 response of the Thru portion of the TRL kit is fairly accurate for the testing setup and the noise that comes along with it.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/S21_Thru_Phase.png)<br>

For some reason I was not able to get the phase to match up for simulated and fabricated. I believe this comes from the errors involved in calculating the length of the Thru line and incorrect implementation.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/PINseriesswitch_S11.png)<br>

The responses match up quite nicely for simulated and measured. The frequency response of each setting of the PIN series switch is extremely close for both simulated and measured S11 responses. The magnitudes would be expected to be different due to various testing factors such as the angle at which it is held or the bend of the cable to which it is attached.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/PINseriesswitch_S21.png)<br>

Once again, the simulations and the measured data matched up nicely for this PIN series switch in the S21 responses. The frequencies are accurate and the magnitude difference can be explained by testing factors.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_5/TRL_Capacitance.png)<br>

## Conclusion
This lab was intended to go through some basic electromagnetic designs for the purpose of simulating and then fabricating and measuring for comparison. TRL calibration kits are important for testing transmission line structures and will be used later in the lab while testing more complex structures. The PIN diode switch was a simple introduction to HFSS with an interesting design that gave a varying response based on adjusting a few parameters.

## Hindsight
I wish I had known a bit more about the PIN diode switch before the lab had started. It took a little bit to understand the design.

## Reflection
David did most of the lab for us so it wasn't particularly challenging. I did, however, learn a lot about Python scripts and rather enjoy how easy it is to create plots from .csv files. 
