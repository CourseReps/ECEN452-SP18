import serial
import time
import numpy as np
import struct


# ---------------------------AD5668 command; 16 bit DAC----------------
CMD_W_n = 0b0000        # Write to input register n
CMD_U_n = 0b0001        # Update DAC register n
CMD_WU_all = 0b0010     # write to input register n, update all; (software nLDAC)
CMD_WU_n = 0b0011       # write to input register n, update n; (software nLDAC)
CMD_POW = 0b0100        # POWer down or POWer up DAC
CMD_CCR = 0b0101        # load Clear Code Register
CMD_nLDAC = 0b0110      # load nLDAC register
CMD_RST = 0b0111        # ReSeT
CMD_REF = 0b1000        # set up internal REF register

DAC_A = 0b0000      # select DAC A
DAC_B = 0b0001      # select DAC B
DAC_C = 0b0010      # select DAC C
DAC_D = 0b0011      # select DAC D
DAC_E = 0b0100      # select DAC E
DAC_F = 0b0101      # select DAC F
DAC_G = 0b0110      # select DAC G
DAC_H = 0b0111      # select DAC H
DAC_ALL = 0b1111    # select DAC ALL

# check data sheet or DAC_cmd_format excel sheet for more info
def DAC_cmd(cmd_type, reg_n, data):
    data_byte = np.empty(4, int)
    data_byte[0] = cmd_type
    # bit-wise and to keep MSB 4 bit, then shift right by 12 bit; bit-wise or to merge with reg_n
    reg_n <<= 4  # bit-wise bit shift to the left by 4
    data_byte[1] = reg_n | ((data & 0b1111000000000000) >> 12)
    # bit-wise and to keep Mid 8 bit, then shift right by 4 bit
    data_byte[2] = (data & 0b0000111111110000) >> 4
    # bit-wise and to keep LSB 4 bit, then shift left by 4 bit
    data_byte[3] = (data & 0b0000000000001111) << 4  # bit-wise and to keep LSB 4 bit

    return data_byte

# -----------------------------------------------------------------------------

port = "COM38"  # bluetooth comm port
baud = 9600     # baud rate of UART
ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_ODD, serial.STOPBITS_ONE, timeout=1)

if ser.isOpen():
    print(ser.name + " is open")
    # get device Vcc
    ser.write(bytes([0xFF]))
    RX_byte = ser.read(2)
    print('RX << ' + str(RX_byte))
    vcc_bit = struct.unpack('H', RX_byte)
    vcc = 1024.0 * 1.1/vcc_bit[0]
    print('device Vcc(V) = ' + str(vcc))

    # DAC default use external reference
    # set up to use internal reference
    # need to run it twice? why?
    for i in range(0,2):
        ser.write(bytes([CMD_REF]))
        ser.read()
        time.sleep(0.1)
        ser.write(bytes([0b0000]))
        ser.read()
        time.sleep(0.1)
        ser.write(bytes([0b0000]))
        ser.read()
        time.sleep(0.1)
        ser.write(bytes([0b0001]))    # set 1 to use internal reference
        ser.read()
        time.sleep(0.1)

    while True:
        cmd_in = input("Volt (V) = ")    # user input
        set_volt = int(cmd_in, 10)   # parse the string as binary
        if set_volt <= vcc:
            TX_bit = set_volt/vcc * 0xFFFF   # 16 bit DAC resolution
            TX_cmd = DAC_cmd(CMD_WU_all, DAC_B, int(TX_bit))
            print("TX >> " + str(int(TX_bit)))
            for j in range(0, len(TX_cmd)):
                ser.write(bytes([TX_cmd[j]]))  # send the byte thru com port
                print('RX << ' + str(ser.read()))   # receive sent byte as feedback
                time.sleep(0.1)
            print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
        else:
            print("error: set voltage is great than Vcc")
            print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
else:
    print("fail to connect to " + ser.name)

ser.close()



