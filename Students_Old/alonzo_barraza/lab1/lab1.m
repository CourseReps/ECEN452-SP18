clc; close all
%% Part 4 *****************************************************************
%% Givens -----------------------------------------------------------------
Z0 = 50;
Z = 10+1j*25;
c = 3*10^8;
f = 2.45*10^9;
lambda = c/f;
l1 = 0.8*lambda;
l2 = 0.25*lambda;
%% ABCD Matrix for a T-Line -----------------------------------------------
A = 1;
B = Z;
C = 0;
D = 1;
%% Conversion -------------------------------------------------------------
A0 = A;
B0 = B/Z0;
C0 = C*Z0;
D0 = D;
delta4 = A0+B0+C0+D0;
%% ABCD to [S] ------------------------------------------------------------
S11 = (A0+B0-C0-D0)/delta4;
S12 = 2*(A0*D0-B0*C0)/delta4;
S21 = 2/delta4;
S22 = (-A0+B0-C0+D0)/delta4;

ABCD = [A B;C D];
S = [S11 S12;S21 S22];
display(ABCD)
display(S)

%% Part 5 *****************************************************************
f0 = 2*10^9; % start frequency
f1 = 3*10^9; % stop frequency
steps = 100; % number of steps
f = f0:steps:f1;
S11_array = zeros(steps,1); % initialize s11 array
S21_array = zeros(steps,1); % initialize s21 array
for i = 1:steps
    lambda = c/f(i);
    beta = 2*pi/lambda;

    theta1 = beta*l1; % length 1
    theta2 = beta*l2; % length 2 

    %% Reference Shift [S] ------------------------------------------------
    S11_prime = S11*exp(-1j*2*theta1);
    S12_prime = S12*exp(-1j*(theta1+theta2));
    S21_prime = S21*exp(-1j*(theta1+theta2));
    S22_prime = S22*exp(-1j*2*theta2);
    S_prime = [S11_prime S12_prime;S21_prime S22_prime];
    display(S_prime)
    S11_array(i,1) = mag2db(abs(S11_prime)); % S11 magnitude in dB
    S21_array(i,1) = mag2db(abs(S21_prime)); % S21 magnitude in dB

    %% [S] to ABCD --------------------------------------------------------
    A_prime = ((1+S11_prime)*(1-S22_prime)+S12_prime*S21_prime)/(2*S21_prime);
    B_prime = Z0*((1+S11_prime)*(1-S22_prime)-S12_prime*S21_prime)/(2*S21_prime);
    C_prime = ((1-S11_prime)*(1-S22_prime)+S12_prime*S21_prime)/(Z0*2*S21_prime);
    D_prime = ((1-S11_prime)*(1+S22_prime)-S12_prime*S21_prime)/(2*S21_prime);
    ABCD_prime = [A_prime B_prime;C_prime D_prime];
    display(ABCD_prime)
end

