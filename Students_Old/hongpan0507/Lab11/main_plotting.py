from mod_read_data import read_measured_data, read_preGRL_data, read_postGRL_data
from mod_plot import meas_rect_plot, preGRL_rect_plot, postGRL_rect_plot

file_name = ['Air', 'Cardboard', 'Plexiglass']
data = read_measured_data(file_name)
meas_rect_plot(file_name, data)

file_name = ['S11_TD_wReflect_preGRLcal']
data = read_preGRL_data(file_name)
preGRL_rect_plot(file_name, data)

file_name = ['S21_Thru_postGRL']
data = read_postGRL_data(file_name)
postGRL_rect_plot(file_name, data)
