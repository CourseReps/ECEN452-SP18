# Lab 5 Report
Matias Kalaswad

In this lab I worked with Chloe Dixon and Matthew Walck. Some of the things that we worked on include parameter calculations, HFSS simulations, lab reports, and plots.

## Background
In this lab we worked with the TRL calibration kit and the PIN diode switch. The TRL kit was designed for frequencies between 1 GHz and 5 GHz. The diode switch is a current-controlled resistor; it can also be described as a semiconductor diode in which a highly resistive intrinsic region is put in between a P-type and N-type region.

## Design
To design the TRL kit we used an online microstrip calculator. The parameters we used are as follow:

	h = 1.575 mm
	er = 4.1
	f = 3 GHz
	Z0 = 50 ohm

The calculator allowed us to find the following values:

	de-embeded: 15 mm
	reflect length, width: 15 mm, 3.17 mm
	thru length, width: 30mm, 3.17 mm
	line length, width: 44.07 mm, 3.17 mm

Given the width of the 50 ohm line as 3.105mm we obtained the following values:

	width of 100 ohm choke = 0.72mm
	quarter wavelength = 17.79 mm

## Procedure
In lab David showed us the calibration of both designs. The TRL kit required solving a third order polynomial with HFSS data and python code.  The coefficients that were found were then entered into the network analyzer and calibrated both ports to the reflect, thru, and line.

After saving the data in a csv file, David did a similar calibration for the PIN diode for both the on and off stages and then saved this data in a csv file.

## Results and Discussion
In the graphs below, S_NM represents the graph where the circuit is being measured at gate N while gate M is being excited. S21 was the parameter that we were most interested in. This is where gate 1 is excited while we measure at gate 2. The lab data yielded very noisy data for the S21 magnitude. It does not match up well with simulated data. The phase data is much cleaner and somewhat matches the simulated data. We can observe that the measured S21 is essentially 0. The PIN diode tests behaved as expected, which can be seen in the plot below.  

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab5/Calibration_Standard_Magnitude.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab5/Calibration_Standard_Phase.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab5/PIN_diode.png)

## Conclusion
The main points of this lab were calculating the lengths and widths of the reflect, thru, and line; as well as calibrating the PIN diode. The results of this lab were favorable for the most part, considering it was our first lab. 

## Hindsight
Working with HFSS for the first time was intimidating and I would have liked to have been better prepared. David's tutorials were very helpful and we were able to get the results we needed with his insights.

## Reflection
The most challenging part of this lab was figuring out how to use HFSS since we have never had any previous experience with it. It was a lot of fun getting into the lab for the first time and having some hands on experience with some of the equipment. 
