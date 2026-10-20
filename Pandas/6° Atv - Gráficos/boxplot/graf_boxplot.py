import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

df = pd.read_csv("dados_boxplot.csv")
fig, ax = plt.subplots(figsize=(8, 4))

sns.boxplot(
    data=df, x="departamento", y="salario",
    palette="Pastel1", ax=ax, hue="departamento", legend=False
)

ax.set_title("Dispersão do Salário por Departamento", fontweight="bold")
plt.tight_layout()
plt.show()