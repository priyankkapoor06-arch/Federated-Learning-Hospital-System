import pandas as pd
import numpy as np

# each row of our data gets converted into an array 

#  Hospital A 
def vectorize_hospital_A(row):
    return np.array([
        row["fever"],
        row["cough"],
        row["breathing_problem"],
        row["chest_pain"],
        row["fatigue"]
    ])


#  Hospital B 
def vectorize_hospital_B(row):
    return np.array([
         row["fever"],
        row["cough"],
        row["breathing_problem"],
        row["chest_pain"],
        row["fatigue"]
    ])


#  Hospital C 
def vectorize_hospital_C(row):
    return np.array([
         row["fever"],
        row["cough"],
        row["breathing_problem"],
        row["chest_pain"],
        row["fatigue"]
    ])