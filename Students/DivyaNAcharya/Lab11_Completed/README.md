# Lab 11: Free Space Measurement with GRL Calibration
Divya Acharya 

## Background
Free-space methods use antennas to focus microwave energy at or through a slab of material without the need for a test fixture. This method is non-contacting and can be applied to materials to be tested under high temperatures and hostile environments. Free space calibration standards present special problems since they are “connector-less”. A calibration can be as simple as a response calibration or as complex as a full two-port calibration depending on the convenience and accuracy desired.  Time domain gating is often used to take the place of or supplement an existing calibration. The GRL (Gated Reflect Line) calibration routine increases the ease of use and reduces the costs associated with TRM and TRL calibration methods. The Gated Reflect Line calibration technique converts a coaxial or waveguide 2-port calibration into a full 2-port free space calibration. Use of this option requires a network analyzer, an appropriate free space fixture, and a metal calibration plate.

##Setup
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab11_Completed/Background.PNG)

##Procedure
1. Two horn antennas (2 GHz to 18 GHz range) are placed facing each other.
2. 2-port SOLT calibration is performed to remove the effect of co-ax cables that connected to the antennas. 
3. Measurements are taken with a metal reflect sheet of same thickness as M.U.T. e.g. Plexiglass, cardboard placed between the antennas. The metal plate acts as a reflect standard.
4. A time domain fourier transform is performed on the data. 

## Results and Discussion

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab11_Completed/er.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab11_Completed/S11Pre.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab11_Completed/S21Post.png)


## Observations
1.What does it mean to transform into the time domain?
<br> Transforming data into time domain helps locate the position of the M.U.T. <br>

2.How do you interpret the S11 data in time domain?
<br> S11 data in time domain represents the position of the M.U.T. in terms of time. The metal reflect is used to establish this location and hence needs to be same thickness as the M.U.T. <br>

3.How does looking at the time domain help with the calibration?
<br> Knowing the location of M.U.T. helps in time gating i.e.zeroing down to the location of the M.U.T. so that accurate measurement cane be taken at that location.<br>

4.What are we looking for when we put the reflect in before performing the calibration?
<br> We are trying to determine the location of of M.U.T. in terms of time<br>

5.How do the three materials measured compare to expectations?
<br> Plexiglass has er in the range 2.2 - 3.4, Air has er=1 and which are values close to observed value. Coudn't find value of er for cardboard.<br>

6. How could we improve the calibration process to get more accurate results?
<br> Steady stands to hold the M.U.T between the horn antennas at the same position instead of holding them by hand would give accurate results.<br>

##Conclusion
Understood how Free Space measurement can be done using GRL calibration.

