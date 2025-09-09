import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('wine_quality.csv')

plt.figure(figsize=(10, 6))
sns.histplot(df['alcohol'], bins=20, kde=True, color='blue')
plt.title('Histograma do Teor Alcoólico no Vinho')
plt.xlabel('Álcool (%)')
plt.ylabel('Frequência')
plt.grid(True)
plt.savefig('histograma_alcool.png')


plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='pH', data=df, hue='quality', palette='Set2', showfliers=False, legend=False)
plt.title('Boxplot de pH Segmentado por Qualidade do Vinho')
plt.xlabel('Qualidade')
plt.ylabel('pH')
plt.grid(True)
plt.savefig('boxplot_ph.png')