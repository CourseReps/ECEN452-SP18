# Lab 5 Report
Chung-Huan Huang 

## Background
In this lab, there are two tasks being simulated: TRL calibration kit and PIN diode switch. The TRL task is to design a calibration kit contains Thru-Reflect-Line microstrip line for calibrating at frequency from 1Ghz to 5Ghz with a center frequency of 3GHz. The second task is to design a PIN diode switch using quarter-wave bias tees to examine performance when diodes are both ON and OFF.

## Design
TRL design:
Calculate the physical width and length of the microstrip lines through microstrip online calculator (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm). With parameters as er = 4.1, h = 1.5748mm, f = 3Ghz, widths can be calculatd as following: <br>
  Width for Z0(50ohm)= 3.115234375 mm <br>
  lambda/4 = 14.03649575801128 mm<br>
  er eff   = 3.1722150398472877 <br>

Therefore, TRL parameters can be implemented into HFSS and start simulating:
Reflect: Width = 3.115234375 mm 
	 length = 15 mm (provide 15mm reference plane beyond the SMA end launch connectors)
Thru: Width = 3.115234375 mm 
      Length = 30 mm (Twice length of Reflect)
Line: Width = 3.115234375 mm 
      Length = 44.03649575801128 mm (Length of Thru plus quarter-wavelength)
Since S21 phase is a slightly different from standart, thus we adjust length to 44.011456 mm

RF PIN Diode design:
Calculate the physical width and length of the microstrip lines through microstrip online calculator (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm). With parameters as er = 4.1, h = 1.5748mm, f = 2.5Ghz, widths can be calculatd as following: <br>
  Width for Z0(50ohm)= 3.1279296875 mm <br>
  Length was given in HFSS<br>

  Width for Z0(100ohm)= 0.745513916015625 mm <br>
  Length(lambda/4) = 17.68371308266564 mm <br>

Before key in above widths and lengths into PIN diode model, we examine those parameters using SCGroundStub and SCBiasStub model for a better matching. Therefore, parameters are slightly fine-tune as following:<br>
  Length for SCGroundStub = 17.65 mm @   S11 = -47.05dB <br>
  Length for SCBiasStub = 18.08 mm @   S11 = -40.28dB <br>

Then put above lengths into PIN diode model and start simulation for both diode ON and OFF.<br>


## Procedure
TRL:
	1. Calculate all parameters such as microstrip width, length and operating frequency we need in HFSS <br>
	2. De-embedding reference plane for each port.<br>
	3. Simulate HFSS file and check Thru and Line phase, if not match with standard then fine-tune length.<br>
	4. Extract Reflect csv file and convert it into capacitance and <br>

PIN diode switch:
	1. Calculate all parameters such as microstrip width, length we need in HFSS <br>
	2. Simulate SCGroundStub HFSS file and fine-tune length for a better matching <br>
	3. Simulate SCBiasStub HFSS file and fine-tune length for a better matching <br>
	4. Record Step 2 and 3 parameters and put those parameters into PINSeriesSwitch model, simulate PINSeriesSwitch model for both diode ON and OFF <br>

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
`![Plot_Name](https://link_to_image_on_github)` <br>
See the raw text of the tutorials for an example.

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
None

## Reflection
The most difficult part of this lab is to fine tune the length for better matching. A slightly change of number may cause a huge result difference. Therefore, it's hard to choose correct number for those fine tune parameters. However, having this chance to go through whole process of designing TRL kit and PIN diode switch makes me understand more about the application of those devices. 
