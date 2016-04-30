

# Lab 11 Report
Mazin M Mustafa 

## Background

In this lab, we will measure the dielectric constants for various solid materials using the following setup. This measurement setup requires GRL calibration

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/Setup.png) <br>

The Free Space Calibration Option increases ease of use and reduces the costs associated with TRM and TRL calibration methods. The Gated Reflect Line (GRL) calibration technique converts a coaxial/waveguide 2-port calibration into a full 2-port freespace [1] calibration. This also requires methemtical model to calculte the permittivity.

## Design

There is no design.

## Procedure

The procedure was performed in the lab by the teaching assistant. As seen from the figure above of the setup of them measurement. The clibration procedure can be generalized to other configurations like having a container for liquids. The GRL calibration consists of SOLT calibration to cancel the effect of cables and connectors. Then the reflect was introduced in the location of the MUT. Then using time gating to focus on a specific delay. The rest of the calibration is done by the software.

## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/Time%20Domain%20S11.png) <br>
fig.2 : Time domain S11

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/Frequency%20Domain%20S21.png) <br>
fig.3 : Frequency domain S21

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/e_prime.png) <br>
fig.4 : e' Measurements 

## Discussion

The time domain transform measures the delay for receiving the reflected wave. The peak value of S11 indicates the MUT location. After applying a time window, this removes the effects of over reflections. The reflect in a calibration standard which helps in determining the location of MUT and also de-embed the free space. Results are close what was expected. 

## Conclusion

## Hindsight

## Reflection

## Reference

[1] http://cp.literature.agilent.com/litweb/pdf/5988-9472EN.pdf 



