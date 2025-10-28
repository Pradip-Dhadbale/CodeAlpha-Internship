
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = pd.read_csv('datasets/country_population.csv')
os.makedirs('output', exist_ok=True)

plt.figure(figsize=(8,6))
sns.scatterplot(data=data, x='GDP(Trillions USD)', y='Population', hue='Continent', s=100)
plt.title('GDP vs Population by Country')
plt.xlabel('GDP (Trillions USD)')
plt.ylabel('Population')
plt.tight_layout()
plt.savefig('output/scatter_gdp_population.png')
print('Saved scatter_gdp_population.png')
