import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("res_dpre.csv")
df['Survived'].value_counts().plot(kind='bar', color=['red', 'green'])
plt.xlabel("Survival")
plt.ylabel("Count")
plt.title("Survival Count")
plt.savefig("vis.png")
print("Visualization saved as vis.png")
