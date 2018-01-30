# Lab 7 Report
Deanna Sessions

## Background
This lab involved fabricating a phase shifter using copper tape and analyzing the response compared to what had been anticipated. In addition to this, a Wilkinson Power Divider was milled and measured using the VNA to compare to our simulated HFSS results.

## Design
The design of the phase shifter was fairly straight-forward with a 50 ohm line with a half wavelength section that gave a 180 degree phase shift on one side and a quarter wavelength section that gave a 90 degree phase shift on the other side. The 180 degree phase shift side was attached with two stubs of 14.07mm and the 90 degree phase shift side was attached with two stubs of 7.03mm. This design could be considered "functional", but we believe that it would have been significantly better had it not been fabricated out of copper tape with our shaky hands.

The Wilkinson Power Divider was a straight-forward HFSS design. This consists of a circular design with two 70.7 ohm legs jutting from a 50 ohm line that meet at a 100 ohm resistor and then separate again. The curve in the line caused a few challenges that required an extra amount of impedance to properly match the line. Based on calculations, the quarter-wavelength of a 70.7 ohm line functioning at 2.5 GHz would require a length of 17.3mm, but this did not garner the proper response so additional length had to be added. The final length of this quarter-wavelength ended up being 24.4mm. 

## Procedure
During lab the phase shifter was designed. This involved calculating the half-wavelength and quarter-wavelength of a 50 ohm line at 2.5 GHz. This resulted in the results included in the design section of this report. These were then implemented on a sheet of FR4 by first creating a 50 ohm line spanning the entire width of the board with connectors on both sides. After the 50 ohm thru line was completed, the board was tested for initial response to compare to the phase shifting. After this, a section was cut out of the center of the line and the stubs were attached at the cuts on either side. The stubs were then connected by a 50 ohm line and soldered together. This was then tested for response and repeated for both 180 degree and 90 degree phase shifting. After this was completed, the thru line was reconnected and measured for the ending response to ensure that the phase of the thru line stayed constant. After the phase shifter data was collected, the milled Wilkinson Power Divider was tested for response.   

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_7/Lab7_PhaseShifter_Thru_Measured.png)<br>
This graph depicts the comparison between the thru line S(2,1) response before and after the phase shifter was implemented.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_7/Lab7_PhaseShifter_Thru_Phase.png)<br>
This graph depicts the comparison between the thru line phase response before and after the phase shifter was implemented.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_7/Lab7_90deg_phase_shift.png)<br>
This graph shows the phase difference between the thru line and the 90 degree phase shift.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_7/Lab7_180deg_phase_shift.png)<br>
This graph shows the phase difference between the thru line and the 180 degree phase shift.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_7/Lab7_Wilkinson_Everything.png)<br>
This graph shows all of the S-parameters of the Wilkinson Power Divider that was designed in HFSS.

## Conclusion
This lab was a clear study of phase shifters and the different methods that can be used to achieve phase shifting. The phase shifter that we fabricated in lab was a challenge due to the copper tape that was being used and our inexperience with small pieces of copper tape and a solder gun. This caused a few problems and gave a response that left a little bit to be desired, but we were able to gain knowledge about how phase shifters would potentially work if they were properly fabricated. The Wilkinson Power Divider also gave a clear example of how microstrip lines can be used as power dividers and also taught us about how to adjust for a circular path of microstrip line in terms of impedance.

## Hindsight
I wish I knew a better technique for using the solder gun.

## Reflection
This lab was brutal. We couldn't get the copper tape to cooperate. Last week we had no issue getting the air flow of the solder gun just right, but this week was very different. We managed to blow our design away on multiple occasions and had to start from scratch many times while also scorching our FR4 board along the way. The actual lab itself wasn't hard, but the implementation of the phase shifter proved to be harder than anticipated.
