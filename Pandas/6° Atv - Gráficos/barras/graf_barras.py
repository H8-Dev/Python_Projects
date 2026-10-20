import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

sns.set_theme(style="whitegrid")
df = pd.read_csv("dados_barras.csv")

fig, ax = plt.subplots(figsize=(10, 4))

sns.barplot(
    data=df,
    x="categoria", y="vendas_medias", hue="regiao",
    palette="Set2", errorbar=None, ax=ax
)

ax.set_title("Médias por categorias e regiões", fontweight="bold")
ax.set_ylabel("Média das Vendas ($)")
ax.legend(title="Categoria")

plt.tight_layout()
plt.show()