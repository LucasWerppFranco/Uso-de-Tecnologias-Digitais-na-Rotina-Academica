import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento dos dados
df = pd.read_excel("dados_tecnologia_academica.xlsx")  # Altere o nome se necessário

# a) Tabela de Distribuição de Frequência (Variável Qualitativa)
print("\nDistribuição de Frequência - Dispositivo Principal:")
print(df['Dispositivo Principal'].value_counts())
print("\nDistribuição relativa (%):")
print(df['Dispositivo Principal'].value_counts(normalize=True) * 100)

# b) Gráficos para variáveis qualitativas
plt.figure(figsize=(12, 5))

# Gráfico 1: Dispositivo Principal (barplot)
plt.subplot(1, 2, 1)
sns.countplot(x='Dispositivo Principal', data=df, palette='Set2')
plt.title('Distribuição do Dispositivo Principal')
plt.xticks(rotation=45)

# Gráfico 2: Sistema Operacional (pie chart)
plt.subplot(1, 2, 2)
df['Sistema Operacional'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='Pastel1')
plt.title('Distribuição do Sistema Operacional')
plt.ylabel('')

plt.tight_layout()
plt.show()

# c) Gráficos para variáveis quantitativas

plt.figure(figsize=(12, 5))

# Gráfico 1: Histograma - Horas de Tela por Dia
plt.subplot(1, 2, 1)
sns.histplot(df['Horas de Tela por Dia'], bins=10, kde=True, color='skyblue')
plt.title('Distribuição das Horas de Tela por Dia')

# Gráfico 2: Boxplot - Trabalhos por Semana
plt.subplot(1, 2, 2)
sns.boxplot(x=df['Trabalhos por Semana'], color='lightgreen')
plt.title('Boxplot de Trabalhos por Semana')

plt.tight_layout()
plt.show()

# d) Medidas de Tendência Central
print("\nMedidas de Tendência Central:")
print("Horas de Tela por Dia:")
print("  Média:", df['Horas de Tela por Dia'].mean())
print("  Mediana:", df['Horas de Tela por Dia'].median())
print("  Moda:", df['Horas de Tela por Dia'].mode().values)

print("\nTrabalhos por Semana:")
print("  Média:", df['Trabalhos por Semana'].mean())
print("  Mediana:", df['Trabalhos por Semana'].median())
print("  Moda:", df['Trabalhos por Semana'].mode().values)

# e) Medidas de Dispersão
print("\nMedidas de Dispersão:")
print("Horas de Tela por Dia:")
print("  Desvio Padrão:", df['Horas de Tela por Dia'].std())
print("  Variância:", df['Horas de Tela por Dia'].var())
print("  Amplitude:", df['Horas de Tela por Dia'].max() - df['Horas de Tela por Dia'].min())

print("\nApps Educacionais por Semana:")
print("  Desvio Padrão:", df['Apps Educacionais por Semana'].std())
print("  Variância:", df['Apps Educacionais por Semana'].var())
print("  Amplitude:", df['Apps Educacionais por Semana'].max() - df['Apps Educacionais por Semana'].min())

# f) Medidas Separatrizes (Quartis, Decis, Percentis)
print("\nMedidas Separatrizes:")
print("Horas de Tela por Dia:")
print("  Quartis:", df['Horas de Tela por Dia'].quantile([0.25, 0.5, 0.75]))
print("  Percentil 90:", df['Horas de Tela por Dia'].quantile(0.9))

print("\nTrabalhos por Semana:")
print("  Quartis:", df['Trabalhos por Semana'].quantile([0.25, 0.5, 0.75]))
print("  Percentil 90:", df['Trabalhos por Semana'].quantile(0.9))

