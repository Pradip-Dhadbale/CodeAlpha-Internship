
import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv('datasets/country_population.csv')
os.makedirs('output', exist_ok=True)

plt.figure(figsize=(10,6))
plt.bar(data['Country'], data['Population']/1e6, color='skyblue')
plt.title('Top Countries by Population (in Millions)')
plt.xlabel('Country')
plt.ylabel('Population (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/bar_chart_population.png')
print('Saved bar_chart_population.png')
