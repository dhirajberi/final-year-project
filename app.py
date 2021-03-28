from flask import Flask,render_template, make_response
from datetime import *
import json
import random
from time import *
import pickle
from flask_mail import Mail, Message
from data import vibration

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'system.maintenance.info@gmail.com'
app.config['MAIL_PASSWORD'] = 'DPR_1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/vibration_data')
def vibration_data():
    time_var = time()*1000
    vibration_data = [time_var, vibration]
    return vibration_data

@app.route('/')
def main():
    vibration = vibration_data()
    vibration = vibration[1]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    pre = model.predict([[vibration]])

    days = int(pre[0])
    hrs = int((pre[0] - int(pre[0])) * 24)
    rul = f'{days} days and {hrs} hrs.'
    percentage = int((days/365)*100)

    if percentage>=30:
        risk = "Safe"
        color = "green"
        return render_template('index.html', vibration=vibration, risk=risk, color=color, current_time=current_time, rul=rul, percentage=percentage)

    elif percentage>0 and percentage<30:
        recipients = ['170390116049@saffrony.ac.in','170390116004@saffrony.ac.in','170390116033@saffrony.ac.in'] #yhaa pe apne 3 ke mail daal do saffrony vaale
        msg = Message('System Alert ', sender = 'riyakh1391999@gmail.com', recipients = recipients)
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S") 
        msg.body = f"Alert at {cur_time}"
        mail.send(msg)
        risk = "Alert"
        color = "Orange"
        return render_template('index.html', vibration=vibration, risk=risk, color=color, current_time=current_time, rul=rul, percentage=percentage)

    else:
        risk = "Fail"
        color = "red"
        return render_template('index.html', vibration=vibration, risk=risk, color=color, current_time=current_time, rul=rul, percentage=percentage)

@app.route('/data')
def data():
    data = vibration_data()
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response    

if __name__ == "__main__":
    app.run(debug=True)
