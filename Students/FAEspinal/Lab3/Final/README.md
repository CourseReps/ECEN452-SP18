#Lab 3

Measured values:
S21(phase)=-41.3281
          =-40.390
S21(Mag dB)= -0.0390625
          = -0.0130208
          =-0.0260417
The values kept changing everytime I ran the code.

##Step 1: Find effective Dielectric

Using the equation given, solve the e_eff.

*c=3E8
+f=3Ghz
+L= 6.44mm
+Theta= 41.3281

e_eff= 3.1777

##Step 2: Find Valid Frequency Range

Rearrange equation given to solve for frequency and plug in 20 and 160 for theta. 

f_Low= 1.45179GHz
f_high= 11.61439GHz

##Step 3: Find Propagation Velocity of the Medium 

Lambda = c/sqrt(e_eff) 
      = 1.682925E8 m/s

##Step 4: Find Attenuation Coefficient

alpha= S21_magnitudedB / L
    = -4.0437 dB/m

Convert

alpha= -35.1239 Np/m


  
