# Lab 8 Report
Abhay Shankar Anand

## Background
Lab 8 consists of the design and analysis of microstrip Hybrid Coupler and Rat Race Coupler

1. __Hybrid Coupler:__ A Hybrid Coupler is designed as described in class with a 3 dB power split on ports 2 and 3 with a phase difference of 90&#176; between them. Port 4 is an isolated port with minimal reflections.
2. __Rat Race Coupler__ A Rat Race Coupler designed with a 3 dB power split on ports 2 and 4, providing a phase difference of 180&#176; between them. Port 3 is an isolated port with minimal reflections.

## Design
### Hybrid Coupler and Rat Race Coupler Design
#### Given constraints
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __f<sub>c</sub>__ = 2.5 GHz
* __Attenuation__ = 3 dB power split
* __Reference Plane__ = 15 mm from edge

### Procedure
#### Hybrid Coupler Design and Implementation

![HybridCoupler](http://microwaves101.a.cdnify.io/images/encyclopedia/images/couplers%20and%20splitters/singlebox.jpg)

Each branchline is designed to be of length **&#955;/4** with impedences **Z<sub>0</sub>** and **Z<sub>0</sub> / &#8730;2**, as specified in the diagram.

As per calculations, the length of **Z<sub>0</sub>** line is 16.95 mm, but to enhance the results, I modified this to ~16.51 mm. All the other values didn't require any tweaking and worked very well.

![HybridCoupler_HFSS](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab8/results/HybridCoupler_HFSS.png)

#### Rat Race Coupler Design and Implementation

![RatRaceCoupler](http://www.antennamagus.com/images/Newsletter5-5/Transition_Microstrip_Ratrace_info_zoom.png)

In a Rat Race coupler, the microsrtip length between ports 1 and 3, 3 and 4, 1 and 2 are **&#955;/4** and between 2 and 4 is **3&#955;/4**, all with impedences  **&#8730;2 Z<sub>0</sub>**.

There was no tweaking of values required.

![RatRace_HFSS](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab8/results/RatRaceCoupler_HFSS.png)

## Results and Discussion
### Results
#### Hybrid Coupler
**Magnitude Plots**
![HybridCoupler_dbPlots](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab8/results/HybridCoupler_dB_Plots.png)

From this plot, we see that ports 2 and 3 provide a 3 dB power split with a good input matching at port 1 and isolation at port 4. There is a slight variation between the milled and simulated results.

**Phase Difference**
![HybridCoupler_PhaseDiff](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab8/results/HybridCoupler_PhaseDiff_Plot.png)

At 2.5 GHz, we get an approximate 90&#176; phase differencve between ports 2 and 3 for both simulated and milled measurements, which conforms with our requirement.

#### Rat Race Coupler
![RatRaceCouplerPlot](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab8/results/RatRaceCoupler_dB_Plots.png)

Ports 2 and 3 provide a power split of about 3 dB. Port 1 is well impedence matched with minimal reflections and port 4 is well isolated from port 1 with about -40 dB at 2.5 GHz. The results are almost identical for milled and simulation measurements except for S11 which shows a broadband response for simulated coupler (not sure why).

### Questions
1. **What modifications did you have to make to the T-line widths/lengths to improve your simulated results?**<br>
For the Hybrid Coupler, I reduced the length of the Y-axis T-line to improve my phase difference result. For the Rat Race coupler however, there was no change made; the results were good with the original design values.
2. **For what applications would each coupler be useful?**<br>
Since the Hybrid Coupler provides a 90&#176; phase difference between ports 2 and 3, it can be used as a Hilbert Transformer for high frequency applications. In many RF receivers, the received modulated signal is multiplied with cos(&#952;) and sin(&#952;) and is processed individually as I and Q components. The Hybrid coupler could be used to generate these signals.
The RatRace couplet could be used for 0&#176; power combining and dividing as well as 180&#176; power combining and dividing.
3. **Why did we put matched loads on the ports while measuring the S-parameters?**<br>
A VNA is a 2 port measurement device whereas our milled components are 4 port. This means that we can only measure 2 ports at a time. When the other ports are not loaded with 50 &#937;, they offer high reflection due to open circuit termination and this would affect the measurements of the 2 connected ports. To minimize these reflections, these unconnected ports are terminated with 50 &#937;

## Conclusion
1. The simulated and milled Hybrid coupler gave results not that different from each other. And we achieved a phase difference of 90&#176; between the two output ports.
2. Rat Race coupler gave almost identical results for the milled and simulated values.

## Hindsight
It would have been very interesting to have seen these components being used as power divider and combiners and would have helped us understand the difference between Hybrid ans Rat Race couplers even better.
