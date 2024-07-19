#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
from sklearn.linear_model import LinearRegression

data = np.loadtxt('trainingdata.txt', delimiter=',')
X = data[:, 0].reshape(-1, 1)
y = data[:, 1]
mask = X[:, 0] <= 4
X_filtered = X[mask]
y_filtered = y[mask]
model = LinearRegression()
model.fit(X_filtered, y_filtered)
def predict_battery_life(charging_time):
    if charging_time <= 4:
        prediction = model.predict([[charging_time]])
        return round(prediction[0], 2)
    else:
        return 8.00

if __name__ == '__main__':
    timeCharged = float(input().strip())
    print(predict_battery_life(timeCharged))
