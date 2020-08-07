import pandas as pd
from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt


# Load CSV and columns
df = pd.read_csv("train_data.csv")

Y = df['ApplicantIncome']
X = df['CoapplicantIncome']


# Split the data into training/testing sets
X_train = X[:-250]
X_test = X[-250:]

# Split the targets into training/testing sets
Y_train = Y[:-250]
Y_test = Y[-250:]


# Plot outputs
fig = plt.gcf()
fig.canvas.set_window_title("Loan Prediction")
plt.scatter(X_test, Y_test,  color='red')
plt.title('Loan Prediction')
plt.xlabel('CoapplicantIncome')
plt.ylabel('ApplicantIncome')
plt.xticks(())
plt.yticks(())

plt.show()