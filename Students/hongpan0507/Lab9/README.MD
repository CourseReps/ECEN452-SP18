# Lab 9 Report
Hong Pan

## Background
Patch antenna is a low profile antenna that is easily built on a flat surface.  
![patch](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/patch.png)

## Design
#### Specification: operating frequency = 3GHz; Z0 = 50ohms; substrate = FR4 (e_r = 4.1); substrate height = 62 mil
1. [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) is used to calculated the characteristic impedance of input microstrip line and quater-wave transformer
2. The length and width of the patch is calculated accoording to the formula below.
![patch formula](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/patch_formula.png)

## Procedure
1. An unmatched patch with 50ohms feed-line is constructed on the substrate.
2. input impedance at 15mm into the feed-line of the patch is measured and recorded.
3. From the measurement of input impedance at 15mm into the feed-line, the input impedance at the design frequency is rotated towards the load on smith chart for at lease one quater-wave length long and until the impedance is purely real.
4. The real impedance is transformed into 50ohms using an quarter-wave transformer is constructed

## Results and Discussion
### Hybrid Coupler
1. From port matching figure, all ports are matched at the design frequency.
2. From port transmission figure, port 2 and port 3 have -3.5dB power split. The extra -0.5dB comes from the loss from the T-line. The s41 has very little power transfer indicates that port 1 and port 4 are isolated.
3. From port transmission phase figure, both simulated result and measured result have 90 degree phase difference between signals at port 2 and port 3 at the design frequency. The simulated reuslt has a minute difference in slope than the measured result.
4. From port isolation figure, port 2 and port 3 are isolated. There is no isolation between port 3 and port 4 or port 2 and port 4. It makes sense because of the symmetry of the structure.
![hybrid_port_matching](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/hybrid_port_matching.png)
![hybrid_port_trans](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/hybrid_port_trans.png)
![hybrid_port_trans_phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/hybrid_port_trans_phase.png)
![hybrid_port_iso](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/hybrid_port_iso.png)


### Rat-race Coupler
1. From port matching figure, all ports are matched at the design frequency.
2. From port transmission figure, port 2 and port 3 have -3.5dB power split. The extra -0.5dB comes from the loss from the T-line. The s41 has very little power transfer indicates that port 1 and port 4 are isolated.
3. From port transmission phase figure, the simulated result has 180 degree phase difference between signals at port 2 and port 3 at the design frequency. The measured result probably contains error.
4. From port isolation figure, port 2 and port 3 are isolated. There is no isolation between port 3 and port 4 or port 2 and port 4. It makes sense because of the symmetry of the structure.
![rat_race_port_matching](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/rat_race_port_matching.png)
![rat_race_port_trans](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/rat_race_port_trans.png)
![rat_race_port_trans_phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/rat_race_port_trans_phase.png)
![rat_race_port_iso](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/rat_race_port_iso.png)

## Conclusion
The symmetry of the device is easily seen by analyzing the s-parameter. The power split is close to -3dB, it will not be -3dB because of the loss of the T-line.
