from math import pi
import csv


# file_name = [csv file name]
# data = [[freq], [e1'], [e2']...]
def read_measured_data(file_name):
    data = []
    for i in range(0, len(file_name)):
        file1 = open(file_name[i]+'.csv', 'rb')  # open the file
        csv_data = csv.reader(file1, delimiter=',')   # convert cvs file to python list
        temp = []
        temp1 = []
        for row in csv_data:   # row contains the row data
            if csv_data.line_num > 1:    # ignore the first line
                if row[0] == 'END':     # check if row reaches the last one
                    break
                if i == 0:  # only record frequency once
                    temp.append(float(row[0])/1e9)  # convert to GHz
                temp1.append(float(row[1]))  # convert to GHz
        if i == 0:  # only record frequency once
            data.append(temp)
        data.append(temp1)

    file1.close()
    return data

# file_name = [csv file name]
# data = [[time], [s11]]
def read_preGRL_data(file_name):
    data = [[], []]
    file1 = open(file_name[0] + '.csv', 'rb')  # open the file
    csv_data = csv.reader(file1, delimiter=',')   # convert cvs file to python list
    for row in csv_data:   # row contains the row data
        if csv_data.line_num > 8:    # ignore the first eight lines
            if row[0] == 'END':     # check if row reaches the last one
                break
            data[0].append(float(row[0])*1e9)  # convert to ns
            data[1].append(float(row[1]))
    file1.close()
    return data

# file_name = [csv file name]
# data = [[time], [s21]]
def read_postGRL_data(file_name):
    data = [[], []]
    file1 = open(file_name[0] + '.csv', 'rb')  # open the file
    csv_data = csv.reader(file1, delimiter=',')   # convert cvs file to python list
    for row in csv_data:   # row contains the row data
        if csv_data.line_num > 8:    # ignore the first eight lines
            if row[0] == 'END':     # check if row reaches the last one
                break
            data[0].append(float(row[0])/1e9)  # convert to ns
            data[1].append(float(row[1]))
    file1.close()
    return data
