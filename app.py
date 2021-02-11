from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from time import time
from random import random
from time import sleep
import pickle

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import serial
import numpy as np
from time import sleep

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

def vibration_data():
    arduino_port = "COM3" 
    baud = 115200  
    ser = serial.Serial(arduino_port, baud)

    #display the data to the terminal
    removerChar="b\'\\rn"

    # def vibration_data():
    while(True):
        
        getData=str(ser.readline())
        for i in removerChar:
            getData = getData.replace(i,"")

        vibration = int(getData)
    
        sleep(1)
        return vibration

# @app.route('/')
# def main():

#     vibration = data()

#     return render_template('index.html', vibration=vibration)
    # arduino_port = "COM3" 
    # baud = 115200  

    # ser = serial.Serial(arduino_port, baud)

    #display the data to the terminal
    # removerChar="b\'\\rn"
    # while 1:
    # getData=str(ser.readline())
    # for i in removerChar:
    #     getData = getData.replace(i,"")

    # vibration = int(getData)

    # vibration = random() * 1000         #vibration change krke real time vaala lena hai
    # pre = model.predict([[vibration]])

    # if pre > 0.7:
    #     risk = "Alert"
    #     color = "red"
    #     return render_template('index.html', risk=risk, vibration=vibration, color=color)

    # else:
    #     risk = "Safe"
    #     color = "green"
    #     return render_template('index.html', risk=risk, vibration=vibration, color=color)

# def vData():
#     arduino_port = "COM3" 
#     baud = 115200  


#     ser = serial.Serial(arduino_port, baud)

#     #display the data to the terminal
#     removerChar="b\'\\rn"
#     # while 1:
#     getData=str(ser.readline())
#     for i in removerChar:
#         getData = getData.replace(i,"")

#     vibration = int(getData)
#     data(vibration)


@app.route('/')
def main():
    vibration = data()
    return render_template('index.html', vibration=vibration)

@app.route('/data', methods=["GET", "POST"])
def data():
    time_var = time() * 500
    vibration = vibration_data()
    data = [time_var, vibration]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response    

if __name__ == "__main__":
    app.run(debug=True)
