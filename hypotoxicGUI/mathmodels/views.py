from django.shortcuts import render
from django.http import HttpResponse
import json
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
# Create your views here.

def extract_file_data(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def data_converter(t,data):
    return [{'x':t[i] , 'y':data[i]} for i in range(len(t))]


data = extract_file_data('/Users/natalliazzz/Downloads/BSU MMF/3coursepaper/A5.json')
coords = data_converter(np.linspace(0, 6, 13),data['Cexp'])

def index(request):
    return render(request,'index.html',{'data' : coords })

def model1(request):
    return render(request,'model1.html',{'t' : list(np.linspace(0, 6, 13)), 'ct' :  list(data['Cexp']),
                                         'gamma': data['gamma'], 'tt':data['T']/1000})

def model2(request):
    return render(request, 'model2.html', {'t': list(np.linspace(0, 6, 13)), 'ct': list(data['Cexp']),
                                           'gamma': data['gamma'], 'tt': data['T'] / 1000})
def model3(request):
    return render(request, 'model3.html', {'t': list(np.linspace(0, 6, 13)), 'ct': list(data['Cexp']),
                                           'gamma': data['gamma'], 'tt': data['T'] / 1000})






