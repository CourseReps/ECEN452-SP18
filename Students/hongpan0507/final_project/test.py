import serial
import time
import numpy as np

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

DAC_VAL = 4096 - 1  # 16 bit DAC value

# check data sheet or DAC_cmd_format excel sheet for more info
def DAC_cmd(cmd_type, reg_n, data):
    data_byte = np.empty(4, int)
    data_byte[0] = cmd_type
    # bit-wise and to keep MSB 4 bit, then shift right by 12 bit; bit-wise or to merge with reg_n
    reg_n <<= 4  # bit-wise bit shift to the left by 4
    data_byte[1] = reg_n | ((data & 0b1111000000000000) >> 12)
    # bit-wise and to keep Mid 8 bit, then shift right by 8 bit
    data_byte[2] = (data & 0b0000111111110000) >> 4
    # bit-wise and to keep LSB 4 bit, then shift left by 4 bit
    data_byte[3] = (data & 0b0000000000001111) << 4  # bit-wise and to keep LSB 4 bit

    return data_byte

port = "COM38"  # bluetooth comm port
baud = 9600     # baud rate of UART

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_ODD, serial.STOPBITS_ONE, timeout=1)

if ser.isOpen():
    print(ser.name + " is open")

    # ser.write(bytes([0xFF]))
    # print('RX << ' + str(ser.read(2)))   # receive sent byte as feedback
    # time.sleep(0.1)

    # DAC default use external reference
    # set up to use internal reference
    for i in range(0, 2):
        ser.write(bytes([CMD_REF]))
        print('RX << ' + str(ser.read()))   # receive sent byte as feedback
        time.sleep(0.1)
        ser.write(bytes([0b0000]))
        print('RX << ' + str(ser.read()))   # receive sent byte as feedback
        time.sleep(0.1)
        ser.write(bytes([0b0000]))
        print('RX << ' + str(ser.read()))   # receive sent byte as feedback
        time.sleep(0.1)
        ser.write(bytes([0b0001]))    # set 1 to use internal reference
        print('RX << ' + str(ser.read()))   # receive sent byte as feedback
        time.sleep(0.1)

    while True:
        cmd_in = input("Byte to send: ")    # user input
        temp = int(cmd_in, 10)   # parse the string as binary

        TX_cmd = DAC_cmd(CMD_WU_all, DAC_B, temp)
        for j in range(0, len(TX_cmd)):
            ser.write(bytes([TX_cmd[j]]))  # send the byte thru com port
            print('RX << ' + str(ser.read().hex()))   # receive sent byte as feedback
            time.sleep(0.1)
        print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))

        # for i in range(0, 65535, 15):
        #     TX_cmd = DAC_cmd(CMD_WU_all, DAC_B, i)
        #     for j in range(0, len(TX_cmd)):
        #         ser.write(bytes([TX_cmd[j]]))  # send the byte thru com port
        #         time.sleep(0.1)
        #     print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
else:
    print("fail to connect to " + ser.name)

ser.close()



