from flask import Flask,render_template, make_response
from datetime import *
# import serial
import json
import random
from time import *
from flask_mail import Mail, Message
import pickle

import numpy as np
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'riyakh1391999@gmail.com'
app.config['MAIL_PASSWORD'] = '9904204686'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

model = pickle.load(open('model.pkl', 'rb')) # Load trained model

@app.route('/vibration_data')
def vibration_data():
    # arduino_port = "COM3" 
    # baud =115200  
    # ser = serial.Serial(arduino_port, baud)
    # #display the data to the terminal
    # removerChar="b\'\\rn"
    # # def vibration_data():
    # getData=str(ser.readline())
    # for i in removerChar:
    #     getData = getData.replace(i,"")

    # vibration = int(getData)
    vibration = random.randint(100,300)
    time_var = time()*1000
    vibration_data = [time_var, vibration]
    return vibration_data

@app.route('/')
def main():
    vibration = vibration_data()
    sleep(2)
    vibration = vibration[1]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    pre = model.predict([[vibration]])  #Predict whether safe or alert
    pre_per = int(pre[0][0]*100)

    if pre >= 0.9:
        risk = "Fail"
        color = "red"
        return render_template('index.html', risk=risk, vibration=vibration, color=color, current_time=current_time, pre_per=pre_per)

    elif pre >= 0.7 and pre < 0.9:
        recipients = ['170390116049@saffrony.ac.in','170390116004@saffrony.ac.in','170390116033@saffrony.ac.in'] #yhaa pe apne 3 ke mail daal do saffrony vaale
        msg = Message('System Alert ', sender = 'riyakh1391999@gmail.com', recipients = recipients)
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S") 
        msg.body = f"Alert at {cur_time}"
        mail.send(msg)
        risk = "Alert"
        color = "orange"
        return render_template('index.html', risk=risk, vibration=vibration, color=color, current_time=current_time, pre_per=pre_per)

    else:
        risk = "Safe"
        color = "green"
        return render_template('index.html', risk=risk, vibration=vibration, color=color, current_time=current_time, pre_per=pre_per)

@app.route('/data')
def data():
    data = vibration_data()
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response    

if __name__ == "__main__":
    app.run(debug=True)