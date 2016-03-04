# Lab 5 Report (Unfinished)
Jared Pocock

## Background
The devices in this lab are a TRL calibration device and a PIN diode. The goal of the lab was to adjust the lengths and widths of the devices until they operate properly at the design frequencies.

## Design
All of the calculations done for this lab were done using the online microstrip calculator at http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm. From the calculator, the microstrip width is about 3.1 mm and the quarter wavelength section for the line section is about 14 mm. For the pin switch, the microstrip line width is about 3.12 mm. All of your calculations go here. Include relevant dimensions and/or diagrams. Comment on any modifications you had to make to your original design after simulation and include you rationale for making these modifications.

## Procedure
For the first part of the lab, the simulation of the TRL was edited so that the microstrip width and the length matched the parameters of a TRL circuit. The reflect line is the reference length, the thru is twice the reference length, and the line length is twice the reference length plus an additional length of a quarter wavelength of the design frequency (3 GHz in this case). The quarter wavelength length was calculated using the online calculator. After the circuit was simulated, graphs were made in Python to compare against the measured data. The same procedure was used for the PIN diode. The microstrip line width and the quarter wavelength length were found using the calculator and inserted into the model and graphs were made of the results. 

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
`![Plot_Name](https://link_to_image_on_github)` <br>
See the raw text of the tutorials for an example.

## Conclusion
The key points to the lab are to understand the various lengths of the TRL circuit and the PIN diode. Knowing how the lengths of the thru, reflect, and line are related makes the lab much simpler to complete. Similarly knowing the lengths of the stubs in the diode circuit should be a quarter wavelength again makes that part of the lab much easier.

## Hindsight
I wish I knew Python better before this lab. It took me a while with the TA's help to figure out how to do plots in Python. 

## Reflection
The most challenging part of the lab was just getting the software to work correctly. I didn't know that the HFSS files had to be pulled from Github, and not just copied from the site. After that, the lab went pretty smoothly.
