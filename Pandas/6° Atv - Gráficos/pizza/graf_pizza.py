import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore


df = pd.read_csv("dados_pizza.csv")

valores = df["faturamento"].to_list()
canal = df["canal_venda"].to_list()
cores = sns.color_palette("Set2")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    valores, labels=canal, autopct="%1.1f%%",
    startangle=90, colors=cores,
    wedgeprops=dict(width=0.6, edgecolor="white")
)

ax.set_title("Distribuição de Faturamento por Canal", fontweight="bold")
plt.tight_layout()
plt.show()