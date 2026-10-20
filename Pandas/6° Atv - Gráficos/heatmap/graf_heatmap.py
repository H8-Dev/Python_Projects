import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore
import pandas as pd #type: ignore

df = pd.read_csv("dados_heatmap.csv")

ordem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
dias = [dia for dia in ordem if dia in df['dia_semana'].unique()]
df['dia_semana'] = pd.Categorical(df['dia_semana'], categories=dias, ordered=True)

fig, ax = plt.subplots(figsize=(8, 4))

df_pivot = df.pivot_table(
    index='horario',
    columns='dia_semana',
    values='movimento_clientes',
    aggfunc='mean'
)

sns.heatmap(
    df_pivot, annot=True, fmt=".2f",
    cmap="coolwarm", linewidths=.5, ax=ax
)

ax.set_title("Matriz de Movimentação durante Funcionamento", fontweight="bold")
plt.tight_layout()
plt.show()