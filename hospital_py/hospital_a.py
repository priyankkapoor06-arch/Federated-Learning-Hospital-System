
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os
from utils import vectorize_hospital_A


# created a new folder as models in our project
os.makedirs("models", exist_ok=True)

# load data into python memory
data = pd.read_csv("hospital_data/hospital_a.csv")


# created empty box/list for inputs and output
X = []
y = []

# vectorization of data (converting each messy row → clean numeric vector)
for _, row in data.iterrows():
    X.append(vectorize_hospital_A(row))
    y.append(row["disease"])

# our brain for this project
model = LogisticRegression()
model.fit(X, y)

# model loaded into model folder
pickle.dump(model, open("models/model_a.pkl", "wb"))

print("Hospital A model trained")