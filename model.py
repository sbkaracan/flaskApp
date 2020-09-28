import pandas as pd 
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error

df = pd.read_csv("data/Advertising.csv")

X = df.drop("Sales",axis=1)
y = df["Sales"]

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X,y)

y_pred = lr.predict(X)

from sklearn.metrics import mean_squared_error

print(np.sqrt(mean_squared_error(y, y_pred)))

pickle.dump(lr, open('regression_model.pkl','wb'))

print("done!")
