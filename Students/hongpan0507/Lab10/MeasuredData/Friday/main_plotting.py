from mod_read_data import read_measured_data
from mod_plot import meas_rect_plot

file_name = ['Acetone','DI_Water','DI_water_20MHz_20GHz', 'Ethylene_Glycol','Hydrocal','Isopropyl_Alcohol',
                 'Pine_sol','Silicone_Fluid','Simple_Green','WD_40']

data = read_measured_data(file_name)

meas_rect_plot(file_name, data)
