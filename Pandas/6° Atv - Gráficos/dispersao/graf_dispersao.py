import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

df = pd.read_csv("dados_dispersao.csv")
fig, ax = plt.subplots(figsize=(8, 4))

sns.scatterplot(
    data=df, x="altura_cm", y="peso_kg",
    hue="sexo", alpha=0.8, ax=ax
)
sns.regplot(data=df, x="altura_cm", y="peso_kg", scatter=False, color="gray", ax=ax)

ax.set_title("Relação entre Peso e Altura", fontweight="bold")
plt.tight_layout()
plt.show()
