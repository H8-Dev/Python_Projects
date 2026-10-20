import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

sns.set_theme(style="whitegrid")
df = pd.read_csv("dados_regressao.csv")

fig, ax = plt.subplots(figsize=(10, 4))

sns.scatterplot(
    data=df, x="renda_mensal", y="gasto_mensal", alpha=0.8, ax=ax
)
sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", scatter=False, color="gray", ax=ax)

ax.set_title("Relação entre Renda e Gasto Mensais", fontweight="bold")
plt.tight_layout()
plt.show()
