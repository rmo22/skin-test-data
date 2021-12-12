import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sn

df=pd.read_csv(r'BMI2.csv')

# df.plot(kind='bar', y="Age")

fig, ax = plt.subplots()
my_scatter_plot = ax.scatter(
df["Age"], #x value
df["Body Mass Index"] #y value
)

# plt.plot(np.unique(df["Moisture"]), np.poly1d(np.polyfit(df["Moisture"], df["Roughness"], 1))(np.unique(df["Moisture"])), color='black')

#below is correct labelling however I want to add a unit symbol for each axis
# ax.set_xlabel("Moisture")
# ax.set_ylabel("Roughness")

#adding units to axes
plt.rcParams["font.family"] = "Times New Roman"
plt.xlabel("Age, years")
plt.ylabel("Body Mass Index")


plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.xlim(0,100)
plt.ylim(0,50)

# c="Moisture"
# d="Rougness"

ax.grid(False)
