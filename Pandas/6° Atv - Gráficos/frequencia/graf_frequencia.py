import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

df = pd.read_csv("dados_frequencia.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    data=df, x="tipo_atendimento",
    bins=15, kde=True,
    color="#2563eb", ax=ax
)

ax.set_title("Frequencia do Tipo de Atendimento", fontweight="bold")
plt.tight_layout()
plt.show()