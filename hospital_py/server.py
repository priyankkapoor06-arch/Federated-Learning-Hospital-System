

import numpy as np
import pickle
import subprocess

print("\n🧠 FEDERATED HEALTH AI SYSTEM STARTED\n")

# ----------------------------
# LOAD HOSPITAL MODELS
# ----------------------------

model_a = pickle.load(open("models/model_a.pkl", "rb"))
model_b = pickle.load(open("models/model_b.pkl", "rb"))
model_c = pickle.load(open("models/model_c.pkl", "rb"))

# Weights = how much that symptom pushes decision toward disease
# Bias = starting position before seeing any symptom / assume healthy


# ----------------------------
# Federated averaging
# ----------------------------

global_w = (model_a.coef_ + model_b.coef_ + model_c.coef_) / 3
global_b = (model_a.intercept_ + model_b.intercept_ + model_c.intercept_) / 3

print("\nMODEL WEIGHTS:")
print(global_w)

print("\nMODEL BIAS:")
print(global_b)


# ----------------------------
# PATIENT INPUT
# ----------------------------

print("\n🧠 ENTER PATIENT SYMPTOMS (0 = No / 1 = Yes)\n")

fever = int(input("Fever: "))
cough = int(input("Cough: "))
breathing_problem = int(input("Breathing Problem: "))
chest_pain = int(input("Chest Pain: "))
fatigue = int(input("Fatigue: "))


# ----------------------------
# ML PREDICTION WHOLE PROCESS
# ----------------------------

X = np.array([[
    fever,
    cough,
    breathing_problem,
    chest_pain,
    fatigue
]])

# DOT PRODUCT (fever × w1) + .....

ml_score = np.dot(X, global_w.T) + global_b
ml_score = ml_score.item()

print("\nML_SCORE: just a raw number")
print(ml_score)
# .item() = converts NumPy single-value array into normal number


# sigmoid any number → probability (0 to 1)
ml_score = 1 / (1 + np.exp(-ml_score))

print("\nML_SCORE: a probabilty value")
print(ml_score)


# ----------------------------
# LIFESTYLE INPUT
# ----------------------------

print("\n🧠 ENTER LIFESTYLE FACTORS (0 = No / 1 = Yes)\n")

stress = int(input("Stress: "))
job_change = int(input("Job Change: "))
moved_city = int(input("Moved City: "))
exercise = int(input("Exercise: "))
good_diet = int(input("Good Diet: "))
checkup = int(input("Regular Checkup: "))


# ----------------------------
# LIFESTYLE HEALTH 
# ----------------------------

#“start from moderately healthy state”
health = 0.6

if stress:
    health -= 0.20

if job_change:
    health -= 0.10

if moved_city:
    health -= 0.05

if exercise:
    health += 0.15

if good_diet:
    health += 0.12

if checkup:
    health += 0.10

# A BONUS AT END 
health += 0.05

# FIXING MAX AND MIN RANGE OF HEALTH VALUE
health = max(0.1, min(0.95, health))


# ----------------------------
# FINAL SCORE
# ----------------------------

final_score = (
    ml_score * 0.75
    +
    (1 - health) * 0.25
)

final_score = max(0, min(1, final_score))


# ----------------------------
# OUTPUT
# ----------------------------

print("\n-------------------")
print("🧠 FINAL REPORT")
print("-------------------")

print("Disease Risk (ML):", round(ml_score, 2))
print("Lifestyle Health risk:", round(1 - health, 2))
print("FINAL RISK SCORE:", round(final_score, 2))


# ----------------------------
# EXPLAINABLE AI
# ----------------------------

print("\n🧠 WHY THIS RESULT?\n")

if ml_score >= 0.7:
    print("- ❗ Strong disease symptoms detected")

elif ml_score >= 0.4:
    print("- ⚠️ Mild disease signals present")

else:
    print("- ✅ Low symptom risk")


if 1 - health >= 0.7:
    print("- ❗ Poor lifestyle")

elif health >= 0.4:
    print("- ⚠️ Average lifestyle")

else:
    print("- ✅ Good lifestyle habits")


if final_score >= 0.70:
    print("Status: 🚨 High Risk")

elif final_score >= 0.45:
    print("Status: ⚠️ Moderate Risk")

else:
    print("Status: ✅ Healthy")


# ----------------------------
# OPEN GRAPH
# ----------------------------

# patient full details in one box

data = [
    fever,
    cough,
    breathing_problem,
    chest_pain,
    fatigue,

    stress,
    job_change,
    moved_city,
    exercise,
    good_diet,
    checkup
]

# run another Python file like a separate program

subprocess.run([
    "python",
    "graph_system/graph_gnn.py",
    *map(str, data)
])