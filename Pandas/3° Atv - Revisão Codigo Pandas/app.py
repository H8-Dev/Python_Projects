import pandas as pd  # type: ignore
import sqlite3

print("=== ETAPA 1: EXTRAÇÃO DE DADOS ===")

# 1. Leitura de arquivo CSV (Lojas físicas)
vendas_loja = pd.read_csv("vendas_loja.csv")
vendas_loja["origem"] = "Física"
vendas_loja["data_venda"] = "2026-09-01"

# 2. Leitura de arquivo Excel (E-commerce)
vendas_site = pd.read_excel("vendas_site.xlsx")
vendas_site["origem"] = "Online"
vendas_site["data_venda"] = "2026-09-02"

# 3. Leitura de arquivo JSON (Cadastro de Clientes)
clientes = pd.read_json("clientes.json")

imposto_regiao = pd.read_json("aliquota.json", typ="series")
imposto_regiao.name = "aliquota_imposto"

# 4. Leitura do Banco de Dados SQLite nativo (Catálogo de Produtos)
with sqlite3.connect("catalogo.db") as conn:
    produtos = pd.read_sql("SELECT * FROM produtos", con=conn)

print("Dados extraídos com sucesso!")

print("\n=== ETAPA 3: TRATAMENTO E INTEGRAÇÃO DE DATAFRAMES ===")

# 1. Concatenação dos DataFrames de vendas
vendas_consolidadas = pd.concat([vendas_loja, vendas_site], ignore_index=True)
series_datas = pd.to_datetime(vendas_consolidadas["data_venda"])
series_dias_semana = series_datas.dt.day_name()

print("\nSeries derivada (Dias da semana):")
print(series_dias_semana)


# 2. Limpeza: Tratamento de nulos na coluna desconto e remoção de duplicadas
vendas_consolidadas["desconto"] = vendas_consolidadas["desconto"].fillna(0.0)
vendas_consolidadas = vendas_consolidadas.drop_duplicates()

# 3. Merges (Cruzamentos com Produtos e Clientes)
df_completo = vendas_consolidadas.merge(produtos, on="produto_id", how="left", indicator="merge_produto")
df_completo = df_completo.merge(clientes, on="cliente_id", how="left", indicator="merge_cliente")

df_completo = df_completo[((df_completo["merge_produto"] == "both")&
                           (df_completo["merge_cliente"] == "both"))].drop(columns=['merge_produto','merge_cliente'])

regras_negocio = (
    (df_completo["desconto"] < 1.0) &
    (df_completo["quantidade"] >= 0) &
    (df_completo["preco_unitario"] >= 0) &
    (df_completo["desconto"] < 0)
)

df_completo = df_completo[regras_negocio].copy()

# 4. Mapeamento: Associando a Series imposto_regiao via coluna 'estado'
df_completo["imposto"] = df_completo["estado"].map(imposto_regiao)

print("DataFrame Puro:")
print(df_completo)
print("DataFrame Integrado e Tratado:")
print(df_completo[["transacao_id", "nome", "nome_produto", "origem", "desconto", "imposto"]])


print("\n=== ETAPA 4: AGREGAÇÃO E MÉTRICAS ===")

df_completo["faturamento_bruto"] = (
    df_completo["quantidade"]
    * df_completo["preco_unitario"]
)

# 1. Criando coluna calculada de Faturamento Líquido
# Fórmula: Quantidade * Preço * (1 - Desconto) * (1 - Imposto)

df_completo["faturamento_liquido"] = (
    df_completo["quantidade"] 
    * df_completo["preco_unitario"] 
    * (1 - df_completo["desconto"]) 
    * (1 - df_completo["imposto"])
)

# 2. Tabela Dinâmica (Pivot Table) com Faturamento por Categoria e Origem
relatorio_final = pd.pivot_table(
    df_completo,
    values="faturamento_liquido",
    index="categoria",
    columns="origem",
    aggfunc="sum",
    fill_value=0.0,
    margins=True,
    margins_name="Total Geral"
)

# Formatação monetária dos resultados da tabela dinâmica
relatorio_formatado = relatorio_final.map(lambda x: f"R$ {x:,.2f}")

print("\n--- RELATÓRIOS FINAIS: FATURAMENTO LÍQUIDO (R$) | TICKET MÉDIO | DESCONTO MÉDIO ---")
print(relatorio_formatado)

ticket_medio = df_completo.groupby(["cliente_id"]).nlargest()
print(ticket_medio)

desc_medio = df_completo.groupby(["categoria"])["desconto"].mean()
print(desc_medio)