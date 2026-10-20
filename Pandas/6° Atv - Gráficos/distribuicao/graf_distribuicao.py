import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

sns.set_theme(style="whitegrid")
df = pd.read_csv("dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    data=df, x="idade",
    bins=15, kde=True,
    color="#2563eb", ax=ax
)

ax.set_title("Distribuição de Idade entre Clientes", fontweight="bold")
plt.tight_layout()
plt.show()