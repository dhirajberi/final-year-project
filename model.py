import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle

df = pd.read_csv('model.csv')
reg = linear_model.LinearRegression()
reg.fit(df[['vibrationMeasurement']], df.remainingTime)

# print(reg.coef_)
# print(reg.intercept_)

# y=-1.40729408*300 + 441.4690342444957
# print(y)

pickle.dump(reg, open('model.pkl', 'wb'))

# prediction = reg.predict([[100]])

# print(prediction[0])

# days = int(prediction[0])
# hrs = int((prediction[0] - int(prediction[0])) * 24)
# print(f'{days} days and {hrs} hrs.')