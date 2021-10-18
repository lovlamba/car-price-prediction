from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create your views here.
def index(request) :
    if request.GET :
        dict = request.GET
        data = list(dict.values())
        try:
            test = [np.array(data, dtype='float64')]

            cars = pd.read_csv("predictor/car.csv")
            x =cars[['curbweight','enginesize','wheelbase', 'carlength', 'carwidth','boreratio','stroke']]
            y = cars['price']
            lm = LinearRegression()
            lm.fit(x, y)

            pred = lm.predict(test)
            pred = pred[0]/1000
            ff = "{:.2f}".format(pred)

            text = 'The price of the car can be ' + str(ff) + ' lakhs.'

            context = {
                'variable': text
            }
            return render(request, 'index.html', context)

        except:
            context = {
                'variable':"Please fill all entries"
            }
            return render(request, 'index.html', context)
    else :
        return render(request, 'index.html')

