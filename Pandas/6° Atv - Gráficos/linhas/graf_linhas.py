import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

sns.set_theme(style="whitegrid")
df = pd.read_csv("dados_linhas.csv")
df["data"] = pd.to_datetime(df["data"])

fig, ax = plt.subplots(figsize=(10, 4))

# Criando o gráfico de linhas
sns.lineplot(
    data=df[df["data"].dt.year == 2026],
    x="loja", y="vendas",
    marker="o", color="#2563eb", linewidth=2, ax=ax
)

ax.set_title("Evolução das vendas em 2026", fontweight="bold")
ax.set_xlabel("Loja")
ax.set_ylabel("Total de Vendas")

plt.tight_layout()
plt.show()