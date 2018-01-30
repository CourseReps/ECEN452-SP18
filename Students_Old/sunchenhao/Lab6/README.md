# Lab6

## Task 1 
### Step 1
  First of all, we can calculate the order N by abs(W/Wc)-1 = abs(f/fc)-1, where f is what we need and fc = 2.5GHz.
  From the figure Attenuatuon Vs abs(W/Wc)-1, we can know the min N is 5.
### Step 2
  Now, we can find the filter coefficients for low pass filter prototype from butterworth element value table,
  these are g1=0.6180 g2=1.6180 g3=2.0000 g4=1.6180 g5=0.6180
### Step 3
  Based on these 5 numbers, we can build prototype ladder network. 
### Step 4
  We can use Richards' Transformation to convert capacitors into OC shunt stubs and SC stubs.
  The impedance of Shunt OC stubs equal to the reverse of filter coefficients, and impedance of Series SC stubs equals to filter cofficients.
### Step 5
  Now we can use Kuroda's identities to convert series stubs to shunt stubs.
  First, insert unit elements at both load and sourse sides, which is both Z0. And Kuroad's identities allow us swith the left unit element and the original left series SC stub.The original Shunt OC stubs is transformed to series SC stub and their impedance follow Kurodas' rules. This allow us to separate shunt stubs and series stubs, and the most important is it allow us transform shunt stubs and series stubs to each other.
  So, after several times of applying Kuroda's identities, we can get 5 shunt OC stubs separated by 4 unit elements, whose impedances are both follow Kuroda's identities.
  Their values are(from left to right): Shunt OC stub 181 Ohm,Unit Element 69 Ohm, Shunt OC stub 43 Ohm,Unit Element 112 Ohm, Shunt OC stub 25 Ohm,Unit Element 112 Ohm,Shunt OC stub 43 Ohm,Unit Element 69 Ohm,Shunt OC stub 181 Ohm. And their length are both 0.125 Lambda.
### Step 6
  This design now can be verified in HFSS 
  General Design is as follow.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL.png)

  Here is main parameters
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_Parameter.png)

  Here are S11 and S21 in dB
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_S11_S21_dB.png)

  Here are S11 and S21' Phase in Degree
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_S11_S21_Phase.png)

Here are some data comparation
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_S11_dB.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_S21_dB.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_S11_Phase(Deg).png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TL_S21_Phase(Deg).png)

### Step 8
  Based on Transmission Line verison, we can transform it into trapped stubs version .
  jZoc = jZ0*cot(Bl)
  We know the Zoc from design process before, then the Zoc of new TS version can be calculated by two new JZoc parallel.
  For example, for the first Shunt OC stub, the jZoc = j181*cot(pi/4). Well, for the new version, jZoc1 = jZoc2 = j89*cot(2pi*x1)
  And then, we can derive x1 by calculating jZoc = jZoc1||jZoc2.
  So, the answer is x1 = 2.669, x2 = 8.9696, x3 = 11.8355, x4 = 8.9696, x5 = 2.669.
  
  Here are general design
  
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS.png)
  Here are main parameters
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_Parameters.png)
  Here are S11 and S21 in dB
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_S11_S21_dB.png)
  Here are S11 and S21's Phase in Degree
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_S11_S21_Phase.png)
  
  Here are some data comparation:

  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_S11_dB.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_S21_dB.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_S11_Phase.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/LPF_TS_S21_Phase.png)

## Task 2
###Step1
  use the table to determine the element values of this filter
###Step2
  Based on these element values, ladder prototype can be built.
###Step3
  COnvert this to a band-stop topology, replace shunt element with shunt LC series networks.
###Step4
  Use inverters(quater-wave transformers) to provide separation between series and shunt elements
###Step5
  Calculate the scaled impedance values of the equivalent OC stubs using Zs = 4Z0/(pi*Delta*gn)
  So all impedance values can be calcuated.They are(from left to right): shun OC 75 Ohm, Inverter 50 Ohm, shun OC 104 Ohm, Inverter 50 Ohm, shun OC 50 Ohm, Inverter 50 0Ohm, shun OC 104 Ohm, Inverter 50 Ohm, shun OC 75 Ohm. And there both 0.25Lambda .
  
  Here are general design
  
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_TL.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_parameter.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_S11_S21_dB.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_S11_S21_Phase.png)
  
  Here are some datas Comparation
  
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_S11_dB.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_S21_dB.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_S11_Phase.png)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab6/BPF_S21_Phase.png)
  
  # Conclusion
  Basicly, all performance are acceptable. Howere LPF_TS version's performance is kind of far away from measurment.
  
  
  
  
  

