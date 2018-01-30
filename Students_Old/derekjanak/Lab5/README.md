Lab 5

Background:

In this week's lab, the students designed a TRL calibration kit and compared measured, theoretical,
and simulated values for the parameters of the design.  TRL kits are important tools for calibration
of high frequency measurement devices through an eight-term error model.  This calibration is
essential, as different high frequency signals react very differently to the leads and cables of
the device and the fixture.

Application:

The TRL kit is a multipurpose calibration kit that is valid over a specific frequency range.  TRL
kits are typically designed to deembed a certain distance into a circuit for the purposes of
investigating the internal component parameters.  The TRL kit designed in this lab was valid over
a frequency range from 1 GHz to 5 GHz and was set to deembed 15 mm into the DUT.

Design:

The following pages show the calculations performed in designing this circuit.

![Calculations](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Lab5_1.jpeg)
![](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Lab5_2.jpeg)

Procedure:

The student viewed a demonstration of the TRL cal kit designed and obtained measurements of the
parameters of the kit.  The student was introduced to HFSS simulation.  The expectations for
future labs were discussed.

Results:

The following plots show the results of simulations and lab measurements.

![Simulated Thru Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Simulated_Thru.png)
The plot shows the simulated Thru parameters.  The minimum reflection falls at a point just shy of 3 GHz, indicating that the simulated line was slightly longer than it should have been.

![Measured Thru Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Measured_Thru.png)
This plot shows the measured Thru parameter S21.  Note that the magnitude of this parameter hovers around 0 dB, in close agreement with both simulated and theoretical results.

![Simulated Reflect Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Simulated_Reflect.png)
The simulated reflect behaves as expected, hovering near 0 dB across the frequency band.  Note the apparently logarithmic response of the reactance in accordance with the theoretical expectation.

![Simulated Line Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Simulated_Line.png)
The line simulation shows a predictably small reflection and a transmission close to unity.  The minima of S11 fall slightly offset from the desired value of 3 GHz, indicating a slight error in line length.

![Measured Line Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Measured_Line.png)
The measured line magnitude hovers near 0 dB, and the measured phase exhibits a fairly linear decline.

![Simulated PIN Diode Switch Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Simulated_Pin_Diode.png)
The pin diode switch behaves as predicted in the simulation at the target frequency of 2.5 GHz, with high reflection and low transmission when the diode is off, and high transmission and low reflection when the diode is on.  

![Measured PIN Diode Switch Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab5/Measured_Pin_Diode.png)
The measured data approximately matches the simulated data, although the peak transmission occurs at around 2.25 GHz, indicative of excess transmission line length.

Conclusion:

In this lab, the student learned to design a basic TRL calibration kit and compared the experimental
performace of this kit with simulated and theoretical results.  The design itself was fairly
straightforward, but the process introduced a steep learning curve.  Navigating GitHub for the
first time proved challenging, and using HFSS for the first time was difficult as well.  However,
these issues were overcome through perseverance.

Hindsight:

In hindsight, I wish that I had had a more solid foundation in software and tools than I did at
the beginning of the lab.  I also would have liked to have seen an example of a full TRL kit
design procedure in advance of the lab.

Reflection:

The most challenging portion of the lab was learning to use all of the various basic tools.  However
it was incredibly rewarding to see the calculated parameters from my theoretical design respond
correctly in practice.
