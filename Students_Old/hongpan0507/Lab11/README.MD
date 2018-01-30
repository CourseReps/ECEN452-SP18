# Lab 11 Report
Hong Pan

## Background
Gated Reflect Line(GRL) calibration uses time gating to remove the interference from connector, unwanted reflection or noise from 
the environment.

## Procedure
1. Standard open, short and load calibration is performed.
2. Two horn antennas are used to perform S21 through free space.
3. GRL calibration is performed.
  + A metal plate that has the same thickness as the meterial under test is inserted in the middle of the horn antennas
    and used as reflect standard
  + "Transform" function from PNA is turned on, and the signal propagation in time domain can be observed
  + Locating the highest S11 in time domain allows placing a time gate that narrows the measurement space to the thickness
    of the metal plating with the center located in the middle of the horn antennas.
4. Dielectric constant of different materials is measured.
  + Cardboard, plexiglass, and air. 

## Results and Discussion
1. The peak from S11 is where the metal is located in time domain. The presence of high reflection after 0ns need to be calibrated out.
![preGRL](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab11/plotting/preGRL.png)

2. The S21 after calibration is great considering the set-up with different possibility of noise and reflection in the lab.
![postGRL](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab11/plotting/postGRL.png)

1. It is expected that the air has dielectric constant close to 1.
![die_meas](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab11/plotting/die_meas.png)

## Conclusion
If the sample size were to be much smaller than the ones used in this lab, circuit board substrates will be the ideal material 
under test.

## Reflection
Time gating is a very interesting technique
