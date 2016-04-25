<b>ECEN 452-500: Ultra High Frequency Techniques</b><br>
Spring 2016 – Prof. Huff<br>
Lab 11 – Free Space Measurement with GRL Calibration<br>

<b><br>Apply the report template to discuss the theory, setup, procedure, and sources of error for the Gated Line Reflect (GRL) calibration. In the results/discussion section, include the following plots:<br>


Background:<br>
In this lab, a Vector Network analyzers (VNA) will be used to measure the free space s-parameter of different kinds of materials. The MUT will be suspended in air and the characteristics of the material such as permitivity, loss etc will be estimated. This method is good for the solid materials such as plastic, glass, metal and so on. The experiment involves two horn antennas, a MUT sampler holder, and some absorbing materials laid on the ground plane.<br>


Procedure:<br>
Before measuring the characteristics of the material, a calibration adjustment should be implemented to improve the estimation precision. There are lots of methods can be used to do the free space calibration such as the TRM, TRL or GRL(Gated Line Reflect). In this work, we would use GRL to calibrate the VNA. First, a normal coaxial line calibration at each port should be implemented such as the load, short and through. Second, a metal plate with known thickness place between the two horn antennas and measure the S11 parameters in time domain. Third, measure the free space through S21 parameters. To implement the GRL calibration, two free space standards are needed to correctly estimate the measurement errors.<br>



S11_TD_wReflect_preGRLcal.csv – This is a plot of the time domain S11 data with the reflect in place. Remember you can see the reflecting sheet as a local maximum at approximately 3.66ns.<br>
Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab11/free_space_s11.png)<br>
Figure - 1<br><br>


S21_Thru_postGRL.csv – This is a plot of the frequency domain S21 data with an empty test fixture. Comment on what the measurement should look like given that the system is calibrated.<br>
Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab11/free_space_through_s21.png) <br>
Figure - 2<br><br>

Air.csv, Cardboard.csv,Plexiglass.csv – Only plot the ε’ data for each material. You can plot the three data sets on the same graph.
Questions to consider for the report:<br>
Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab11/dielectric_constant_materials.png)<br>
Figure - 3<br><br>


What does it mean to transform into the time domain?<br>
Ans:<br>
When look at the time domain plot, the highest S11 values means the EM wave have biggest reflection. In this case, the highest point of S11 at 0.4 ns is when the wave hits the metal plane. After observe the highest reflection point, we can record the time delay and use to calibrate the VNA. In other words, we can precisely known the position of the MUT plane. That's the main reason why we choose to use the time domain instead of the frequency domain.<br>



How do you interpret the S11 data in time domain?<br>
Ans:<br>
As mentioned above, the highest S11 values means the propogating wave encounters the metal plane. As a result, wave propogates 0.4 ns and hits the metal plane.<br>




How does looking at the time domain help with the calibration?<br>
Ans:<br>
When we known the position of the MUT plane, we can measure the characteristics of the MUT next time.<br> 





What are we looking for when we put the reflect in before performing the calibration?<br>
Ans:<br>





How do the three materials measured compare to expectations?<br>
Ans:<br>
After look up the dielectric constant values of the three materials, we found the plexiglass should be 2.6 @ 3 GHz, paper is around 2.2~3.1 and air is 1. The measured dielectric constant of the cardboard is a little bit lower than the expected value; otherwise other materials are very close to the expecation.<br>




How could we improve the calibration process to get more accurate results?<br>
Ans:<br>
Methods like diminish the multi-path reflection, horn antennas fixed alignment and a good material holder will help increase the accuracy.<br>










Conclusion:<br>

1. In this lab, a free space method is used to estimate the characteristics of different materials. The permittivity, loss tangent and so on can be derived through different frequency spectrum.<br>
2. .<br>



</b>
