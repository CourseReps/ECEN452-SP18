# Lab 6 Report
Francisco A. Espinal

## Background

We design two filters a maximally flat low pass and equi-ripple band stop filter. These filters accept desired signals and reject signals outside the operation band. To design them we must find the order (N) of the filter and using this information construct a Ladder network.  Then additional transformations, such as Richard’s transformation, and Kuroda identities can be used to calculate the components needed like the transmission lines and stubs.      


## Design

First I calculated the order (N). Using the information given I plug it into the |w/w_c|-1 equation and got 0.3. I looked it up on the graph with the attenuations, and determined that the order was 5. From here I followed the steps given to us in the lab walking us through the transformation. Once they were transformed I calculated the widths and lengths of the t-lines. 
     
To calculate the width and effective dielectric of each device I used an online calculator. (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) Thickness used was 62mil. To get the actual physical lengths I used the equation below.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>
I plug in the effective dielectric, frequency, and 45 for theta because we wanted the half of a quarter wavelength. I preformed the same method of calculations for both designs.
 
Max Flat LPF

|      | Width (mm) | E_eff | Physical Length (mm) | Frequency (GHz) | Z_0(ohm) | E_r | 
| -------- |:------:|:---:|:------:|:-------:|:-----:|:-------:| 
| w0        |   3.105468    |   |        |   2.5     |   50   |   4.1     |  
| w1         |   0.067573 |  2.6019    |   7.749    |   2.5    |  181   |   4.1     |
| w2        |   3.93872 |  3.2134    |   6.97312  |   2.5   |   43   |   4.1     |
| w3      |   8.371093 |  3.471142 |   6.7092  |   2.5     |   25   |   4.1     |
| w4       |   3.93872 |  3.2134  |   6.97312   |   2.5     |   43   |   4.1     |
| w5       |   0.067573 |  2.6019    |   7.749       |   2.5     |   181  |   4.1     |
| wUE1        |   0.517578 |  2.8003    |   7.4697  |   2.5   |   112   |   4.1     |
| wUE2     |   0.517578 |  2.8003|   7.4697 |   2.5     |   112  |   4.1     |
| wUE3      |   1.736450 |  2.99598  |   7.2217   |   2.5     |   69   |   4.1     |
| wUE4      |   1.736450 |  2.99598   |   7.2217      |   2.5     |   69   |   4.1     |

I used the equation L=(1/2*pi)tan^-1(89/2*Z_0) to find the lengths of the lines. 

Max Flat LPF Tapped Stubs

|      | Width (mm) | E_eff | Physical Length (mm) | Frequency (GHz) | Z_0(ohm) | E_r | 
| -------- |:------:|:---:|:------:|:-------:|:-----:|:-------:| 
| w0        |   3.105468    |   |        |   2.5     |   50   |   4.1     |  
| w1         |   1 |  2.8891 |   2.19832    |   2.5    |  89   |   4.1     |
| w2         |   1 |  2.8891 |   7.3182812    |   2.5    |  89   |   4.1     |
| w3         |   1 |  2.8891 |   9.656379    |   2.5    |  89   |   4.1     |
| w4         |   1 |  2.8891 |   7.3182812   |   2.5    |  89   |   4.1     |
| w5         |   1 |  2.8891 |   2.19832    |   2.5    |  89   |   4.1     |
| wUE1        |   0.517578 |  2.8003    |   7.4697  |   2.5   |   112   |   4.1     |
| wUE2     |   0.517578 |  2.8003|   7.4697 |   2.5     |   112  |   4.1     |
| wUE3      |   1.736450 |  2.99598  |   7.2217   |   2.5     |   69   |   4.1     |
| wUE4      |   1.736450 |  2.99598   |   7.2217      |   2.5     |   69   |   4.1     |


equi- ripple BSF

|      | Width (mm) | E_eff | Physical Length (mm) | Frequency (GHz) | Z_0(ohm) | E_r | 
| -------- |:------:|:---:|:------:|:-------:|:-----:|:-------:| 
| w0        |   3.111328    |   |     14.1177   |   2.25     |   50   |   4.1     |  
| w1         |   1.462951 |  3.135823 |   14.54179    |   2.25    |  75   |   4.1     |
| w2         |   0.64819 |  2.95559 |   14.8733    |   2.25    |  104  |   4.1     |
| w3         |   3.111328 |  2.82529 |   14.1177    |   2.25    |  50   |   4.1     |
| w4         |   0.64819 |  2.95559 |   14.8733   |   2.25    |  104  |   4.1     |
| w5         |   1.462951 |  3.135823 |   14.54179    |   2.25    |  75   |   4.1     |




## Procedure
Provide a step-by-step decription of the activities you performed during the lab.

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
`![Plot_Name](https://link_to_image_on_github)` <br>
See the raw text of the tutorials for an example.

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
