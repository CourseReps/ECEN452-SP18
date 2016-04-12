# Lab X Report
Hong Pan

## Background
1. Hybrid Coupler is a 4 port symmetric device that splits power equally with 90 degree of phase shift.
![Hybrid](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/hybrid.jpg)
2. Rat-race Coupler has 2 operation mode
  + power split: 
      + divide input power from port 1 equally with 180 degree of phase shifte between port 2 and port 3. Port 4 is isolated.
      + divide input power from port 2 equally with 0 degree of phase shifte between port 1 and port 4. Port 3 is isolated.
  + combine input signal from port 1 and 4
      + summed output is at port 2
      + substracted output is at port 3
![rat race](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/rat_race.jpg)      
  
## Design
### Hybrid Coupler
#### Specification: operating frequency = 2.5GHz; Z0 = 50ohms; substrate = FR4 (e_r = 4.1); substrate height = 62 mil
1. All T-line impedance is 50ohms except the vertical section; its impedance is 1/sqrt(2)*50ohms
2. [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) is used to calculated the microstrip line parameter
3. All parameter is simulated in ADS
4. The same parameter is inputted into HFSS. Minute tuning is required to get the structure to operate at 2.5GHz

### Rat-race Coupler
#### Specification: operating frequency = 2.5GHz; Z0 = 50ohms; substrate = FR4 (e_r = 4.1); substrate height = 62 mil
1. All T-line impedance is 50ohms except the vertical section; its impedance is 1/sqrt(2)*50ohms
2. [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) is used to calculated the microstrip line parameter
3. All parameter is simulated in ADS
4. The same parameter is inputted into HFSS. No tuning is required to get the structure to operate at 2.5GHz

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
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
