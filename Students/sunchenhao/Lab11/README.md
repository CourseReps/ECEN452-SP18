#Lab 11 Report
Chenhao Sun

##Background
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab11/slide_19.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab11/slide_20.jpg) <br>
[1] <br>
Free-space methods use antennas to focus microwave energy at or through a slab of material without the need for a test fixture . This method is non-contacting and can be applied to materials to be tested under high temperatures and hostile environments. Figure upon shows typical freespace measurement setups. Calibrating the network analyzer for a free space measurement is challenging. Free space calibration standards present special problems since they are “connector-less”. A calibration can be as simple as a response calibration or as complex as a full two-port calibration depending on the convenience and accuracy desired. A TRL (Thru-Reflect-Line) or TRM (Thru-Reflect-Match) calibration may actually be easier than other calibration techniques in free space[1].<br>
Time domain gating is often used to take the place of or supplement an existing calibration. There is an optional free space
calibration routine called GRL (Gated Reflect Line). This calibration routine increases the ease of use and reduces the costs associated with TRM and TRL calibration methods. The Gated Reflect Line calibration technique converts a coaxial or waveguide 2-port calibration into a full 2-port free space calibration. Use of this option requires a PNA Series network analyzer with the time domain option, an appropriate free space fixture, and a metal calibration plate. This option also includes a gated isolation/
response calibration, which reduces errors from diffraction effects at the sample edges and multiple residual reflections between the antennas[1]. <br>  
##Design
There are two horn antennas used for Free-space measurement, the ground plane between two horn antennas is paved with absorbing boudary to reduce effects from reflection wave.  A VNA, a metal sheet, two forms are used to perform GRL calibration. 
##Procedure
GRL calibration was performed by TA, and then fixtures was measured. TA also show us how Frequency Select Sheet(FSS) works.Finaly, we had a little visit in the big microwave chamber. 
##Results
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab11/S11_TD_wReflect_preGRLcal.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab11/S21_Thru_postGRL.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab11/e.png) <br>

## Discussion
Transforming data into time domain could help us to determine the distance between antenna and fixture. The peak of S11 in time domain represent the position of fixture. We can apply a time window to remove all other signal's influence. Metal sheet represent the position and thickness of our fixture. The measurement of these there material are close to what we expect. Now we only use absorbing boundary in the ground plane so there are reflection from other thing. We can do the measurement in microwave chamber, so that we can remove basically all other undesirable reflection.

##Conclusion
GRL and freespace measuring is successfully performed.

##Reference
[1]"Agilent Basics of Measuring the Dielectric Properties of Materials ,Application Note". http://www3.imperial.ac.uk/pls/portallive/docs/1/11949698.PDF
