# Lab 5: TRL & Bias Tee
Divya Acharya 

#Task1: Design of a TRL calibration kit

## Background
TRL (Thru, Reflect, Line) represents a family of calibration techniques that measure two transmission standards and one reflection standard to determine the 2-port 12-term error coefficients.TRL Cal is most often performed when you require a high level of accuracy and do not have calibration standards in the same connector type as your DUT.

## Design
**Given:**
- Substrate Dielectric constant er = 4.1
- Substrate Dielectric Loss Tangent tan∂ = 0.01
- Substrate thickness=62mil (~1.57mm)
- Characteristic impedance of strips=50Ω
- Frequency range= 1GHz to 5GHz
- Center frequency= (f1+f2)/2 = (1+5)/2 =3GHz
- Distance to reference plane=15mm

**Values:**

| Standard | Length |
| --- | --- |
| Thru | 30mm |
| Reflect | 15mm |
| Line (Calculated) | 44.06mm |
|Line (Simulated)|43.8mm|
|Width (Calculated)|3.09mm|
|Width (Simulated)|3.37mm|

##Procedure
1. David demonstrated the TRL calibration for Network Analyzer(NA) using the kit he designed and fabricated.
2. Steps in NA: Select Response->Cal->Cal Kit->Edit Kit->Enter Kit Name->Enter Kit Description. Choose Connector->SMA female and Freq Range 1GHz to 5GHz.
3. Coefficiencts corresponding to Reflect standard calculated using Python curve fitting program is entered in NA
4. Set OPEN (for Reflect standard), Set THRU for 0 delay THRU standard and then set THRU again for Line. (Rename this THRU to LINE)
5. Stimulus->Sweep->4001 points; Response->Cal->Start Cal
6. Select the TRL kit created.
7. Save data in .csv file for each calibration
8. For simulation in HFSS, change the width and lengths of the strips to calculated values and vary the lengths until optimum results are obtained.
9. De-embedding the port to reference plane is important to get correct results.
10. Export the Im(Z) plot data of Reflect standard to be used by Python program to find the 3rd order polynomial that fits the capacitance data

## Results and Discussion

## Observations
1. To obtain a Z0 close to 50Ω, width had to be modified to 3.37mm. 
2. Phase of 89.76 degrees was obtained for line with λ/4 = 13.8mm. 
3. Slight changes in length of Line led to inversion of phase sign.
4. 89.76 was the closest that was obtained iteratively changing values of line.

## Conclusion
HFSS & measured results were almost identical for the TRL calibration kit.
