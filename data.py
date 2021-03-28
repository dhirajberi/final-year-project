import serial
arduino_port = "COM3" 
baud = 115200  
ser = serial.Serial(arduino_port, baud)
#display the data to the terminal
removerChar="b\'\\rn"
# def vibration_data():
getData=str(ser.readline())
for i in removerChar:
    getData = getData.replace(i,"")
vibration = int(getData)