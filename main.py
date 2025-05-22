# --------------------------
# INSTRUÇOES PARA RODAR A VENV
# ----------------------------
# python -m venv venv
# venv\Scripts\activate.bat
# pip install pandas matplotlib seaborn openpyxl
# ----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_excel("dados_tecnologia_academica.xlsx")

# Renomear colunas para facilitar
df.columns = [
    "Timestamp", "Dispositivo", "Sistema", "App_Organizacao", "Preferencia_Aula",
    "Horas_Tela", "Qtd_Dispositivos", "Qtd_Apps", "Qtd_Trabalhos"
]

# Padronizar e converter variáveis quantitativas para numéricas
horas_map = {
    "Entre 1 a 3 horas": 2,
    "Entre 3 a 6 horas": 4.5,
    "6 horas ou +": 7
}
df["Horas_Tela_Num"] = df["Horas_Tela"].map(horas_map)

dispositivos_map = {
    "1": 1, "2": 2, "3": 3, "4 ou +": 4
}
df["Qtd_Dispositivos_Num"] = df["Qtd_Dispositivos"].replace(dispositivos_map).astype(int)

apps_map = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5 ou +": 5
}
df["Qtd_Apps_Num"] = df["Qtd_Apps"].replace(apps_map).astype(int)

trabalhos_map = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5 ou +": 5
}
df["Qtd_Trabalhos_Num"] = df["Qtd_Trabalhos"].replace(trabalhos_map).astype(int)

# --- a) Tabela de Frequência
print("\nDistribuição de Frequência - Preferência de Aula:")
print(df["Preferencia_Aula"].value_counts())
print("\nDistribuição relativa (%):")
print(df["Preferencia_Aula"].value_counts(normalize=True) * 100)

# --- b) Gráficos para variáveis qualitativas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.countplot(x="Dispositivo", data=df, palette="Set2")
plt.title("Dispositivo mais utilizado")
plt.xticks(rotation=30)

plt.subplot(1, 2, 2)
df["Sistema"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90, cmap="Pastel1")
plt.title("Sistema Operacional mais usado")
plt.ylabel("")

plt.tight_layout()
plt.show()

# --- c) Gráficos para variáveis quantitativas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df["Horas_Tela_Num"], bins=5, kde=True, color='skyblue')
plt.title("Distribuição de Horas de Tela por Dia")

plt.subplot(1, 2, 2)
sns.boxplot(x=df["Qtd_Trabalhos_Num"], color="lightgreen")
plt.title("Boxplot de Trabalhos por Semana")

plt.tight_layout()
plt.show()

# --- d) Medidas de Tendência Central
print("\nMédias, Medianas e Modas:")
print("Horas_Tela_Num - Média:", df["Horas_Tela_Num"].mean(), 
      "| Mediana:", df["Horas_Tela_Num"].median(), 
      "| Moda:", df["Horas_Tela_Num"].mode().values)

print("Qtd_Trabalhos_Num - Média:", df["Qtd_Trabalhos_Num"].mean(), 
      "| Mediana:", df["Qtd_Trabalhos_Num"].median(), 
      "| Moda:", df["Qtd_Trabalhos_Num"].mode().values)

# --- e) Medidas de Dispersão
print("\nDispersão:")
print("Horas_Tela_Num - Desvio Padrão:", df["Horas_Tela_Num"].std(), 
      "| Variância:", df["Horas_Tela_Num"].var(), 
      "| Amplitude:", df["Horas_Tela_Num"].max() - df["Horas_Tela_Num"].min())

print("Qtd_Apps_Num - Desvio Padrão:", df["Qtd_Apps_Num"].std(), 
      "| Variância:", df["Qtd_Apps_Num"].var(), 
      "| Amplitude:", df["Qtd_Apps_Num"].max() - df["Qtd_Apps_Num"].min())

# --- f) Separatrizes (Quartis e Percentis)
print("\nQuartis e Percentis:")
print("Horas_Tela_Num - Quartis:")
print(df["Horas_Tela_Num"].quantile([0.25, 0.5, 0.75]))
print("Percentil 90:", df["Horas_Tela_Num"].quantile(0.9))

print("Qtd_Trabalhos_Num - Quartis:")
print(df["Qtd_Trabalhos_Num"].quantile([0.25, 0.5, 0.75]))
print("Percentil 90:", df["Qtd_Trabalhos_Num"].quantile(0.9))

