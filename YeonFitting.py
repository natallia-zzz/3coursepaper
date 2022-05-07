import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import json

def extract_file_data(path):
	f = open(path)
	data = json.load(f)
	f.close()
	return data


def func(x, mu, beta):
	return np.exp(0.053*x[0] + x[1]*mu*(1 - np.exp(-beta * x[0])-beta*x[0])/(beta**2))


x, t = np.linspace(0, 6, 13), np.linspace(0,15,4)
X, T = np.meshgrid(x, t)
size = X.shape
x_1d = X.reshape((1, np.prod(size)))
t_1d = T.reshape((1, np.prod(size)))
x_data = np.vstack((x_1d, t_1d))

dataA0 = extract_file_data('yeon-data/A0.json')
dataA5 = extract_file_data('yeon-data/A5.json')
dataA10 = extract_file_data('yeon-data/A10.json')
dataA15 = extract_file_data('yeon-data/A15.json')

data = dataA0['Cexp']+ dataA5['Cexp'] + dataA10['Cexp']+ dataA15['Cexp']
ydata = [i/100 for i in data]
#popt, pcov = curve_fit(func, x_data, ydata)
#popt, pcov = curve_fit(func, x_data, ydata,p0 = [0.0469,0.185])
#popt, pcov = curve_fit(func, x_data, ydata, p0 = [0.0469,0.185], bounds = ([0.01,0.1],[0.1,0.7]))
#popt, pcov = curve_fit(func, x_data, ydata, bounds = ([0.01,0.1],[0.1,0.7]),method = 'trf',loss = 'huber')
# popt, pcov = curve_fit(func, x_data, ydata,p0 = [0.0469,0.185], bounds = ([0.01,0.1],[0.1,0.7]), method = 'trf', tr_solver = 'lsmr',)
popt, pcov = curve_fit(func, x_data, ydata,p0 = [0.0469,0.185], bounds = ([0.01,0.1],[0.1,0.7]),method = 'trf', loss = 'huber', ftol = 1e-10, tr_solver = 'lsmr',)


print('fit: mu=%5.3f, beta=%5.3f' % tuple(popt))

y_est = func(x_data, *popt)

print('error: '+str(np.sum(np.abs(np.array(ydata)-np.array(y_est)))))
