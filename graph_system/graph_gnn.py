# sys = bridge between Python file and command-line
import sys
#This is your GRAPH MAKER library
import networkx as nx
# This is your DRAWING + DISPLAY tool
import matplotlib.pyplot as plt

print("GRAPH SYSTEM STARTED")

# ----------------------------
# RECEIVE VALUES
# ----------------------------

# sys.argv-- contains our inputs
values = list(map(int, sys.argv[1:]))

labels = [
    # disease
    "Fever",
    "Cough",
    "Breathing",
    "Chest_Pain",
    "Fatigue",

    # lifestyle
    "Stress",
    "Job_Change",
    "Moved_City",
    "Exercise",
    "Good_Diet",
    "Checkup"
]

# values = real patient data
# labels = names of those inputs

n = min(len(values), len(labels))

# ----------------------------
# CREATE GRAPH
# ----------------------------

# empty graph 
G = nx.Graph()

# Patient is the main character
patient = "Patient_1"

# This adds the patient into graph
G.add_node(patient)

# i = index (position)
# labels[i] = item at that position

for i in range(n):
    G.add_node(labels[i])

# ----------------------------
# CONNECT ONLY ACTIVE NODES
# ----------------------------

for i in range(n):

    if values[i] == 1:

        G.add_edge(
            patient,
            labels[i]
        )

# ----------------------------
# COLORS
# ----------------------------

colors = []

# go through every point (node) in the graph one by one
for node in G.nodes():

    if node == patient:

        colors.append("red")

    elif node in [
        "Fever",
        "Cough",
        "Breathing",
        "Chest_Pain",
        "Fatigue"
    ]:

        colors.append("orange")

    else:

        if node in [
            "Exercise",
            "Good_Diet",
            "Checkup"
        ]:

            colors.append("green")

        else:

            colors.append("lightblue")

# ----------------------------
# NODE SIZE
# ----------------------------

sizes = []

for node in G.nodes():

    if node == patient:

        sizes.append(3500)

    else:

        sizes.append(2200)

# ----------------------------
# DRAW
# ----------------------------

# open a blank drawing board of size 12x8
plt.figure(figsize=(12, 8))

# “decide where each node should sit in the graph”
pos = nx.spring_layout(
    G,
    seed=42,
    k=2
)
#seed=42
# same layout every time (stable graph)

#k=2
# spacing between nodes (more space)


# actually draws your graph on screen
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=sizes,
    font_size=10,
    font_weight="bold"
)

# Title of graph
plt.title(
    "Patient Health Graph",
    fontsize=16
)

# # prevents overlap, makes graph clean
# plt.tight_layout()
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# # SHOW graph
plt.show()