# Lab 3 Report
Thomas Darden

## Background
For this lab, we are going to calculate the properties of a TRL kit by analyzing the S21 and S21 phase properties measured from the network analyzer. The properties we need to find for the kit are the valid frequency range, effective dielectric constant, propagation velocity, and attenuation coefficient. We are only calculating this from the data given and will not be constructing anything within the lab.

## Design
Let us first find the effective dielectric constant of the kit. The frequency which we are going to consider for the data is 3GHz as it is in the middle of the sweep we recieved from the network analyzer. A useful equation we can use to find it is shown below:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab3/Equation.png)<br>

Let us first solve this equation for the dielectic constant.

Eff = ((c/(l*f))(theta/360))^2

From this equation, we know from the given data that f=3GHz, length = 6.44mm (the addition through length), and the phase (given by the measure data) is -40.8388 degrees. We can plug this into the equation to find:

Eff = 3.10291

From the dielectric constant, we can find the propogation velocity. The equation that denotes that is given below:

V_phase = c/sqrt(Eff)

From the dielectric constant we found, we solve the propogation velocity to be 1.703e8.

Now let us find the valid frequency range of the kit. Using the equation we used to find the dielectric constant, we can solve for f to be:

f = (c/(l*sqrt(Eff)))(theta/360)

To find the lower end of the frequency range, we use theta = 20, and for the higher end we use theta = 160. Solving the equation above with these values of theta and the dielectric constant we used, we find:

f_low = (3e8/(6.44e-3*sqrt(3.102)))(20/360) = 1.469e9 Hz

f_high = (3e8/(6.44e-3*sqrt(3.102)))(160/360) = 11.753e9 Hz

This means that our kit is valid within the frequency range of 1.469GHz and 11.753GHz.

To find the attenuation coefficient, we look at the S21 parameter at 3GHz and convert it to Np.

S21 = -0.029361164 dB = -0.0033803289 Np

We then must find the coefficient in Np per meter by using a proportion:

-0.0033803289/6.44e-1 = a/1

Solving for a, we find the coefficient a = -.5249 Np/m

## Procedure
Solve the equations described in the Design section.

## Results and Discussion
Here are the plots of the data we recieved from the network analyzer.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab3/S21Data.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab3/S21Phase.png)<br>

## Conclusion
From this lab, I was able to see how a network analyzer can compute the properties of a TRL kit from the S21 parameters of a frequency sweep. I learned how the relationship of the properties work.

## Hindsight
N/A

## Reflections
Overall, this was a straightforward assignment that increased my knowledge of how the network analyzer works and how to relate the properties of the TRL kit. There were no real challenges encountered within this lab.

