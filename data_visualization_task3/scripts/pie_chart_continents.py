
import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv('datasets/country_population.csv')
os.makedirs('output', exist_ok=True)

continent_data = data.groupby('Continent')['Population'].sum()

plt.figure(figsize=(7,7))
plt.pie(continent_data, labels=continent_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Population Share by Continent')
plt.tight_layout()
plt.savefig('output/pie_chart_continents.png')
print('Saved pie_chart_continents.png')
