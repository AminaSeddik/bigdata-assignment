import pandas as pd

df = pd.read_csv("res_dpre.csv")
insights = [
    f"Total passengers: {len(df)}",
    f"Survival rate: {df['Survived'].mean():.2f}",
    f"Average age: {df['Age'].mean():.2f}"
]
for i, insight in enumerate(insights, 1):
    with open(f"eda-in-{i}.txt", "w") as f:
        f.write(insight)
print("EDA insights saved!")
