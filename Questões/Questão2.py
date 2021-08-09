import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

sns.pairplot(df, hue='species')
plt.show()

plt.figure(dpi=100, figsize=(10, 3))
sns.scatterplot(x='petal_length', y='species', data=df)
plt.show()

plt.figure(dpi=100, figsize=(15, 5))
sns.boxplot(x='petal_length', y='species', data=df)
plt.show()

df.describe()

df0 = df['species'] == 'setosa'
df1 = df['species'] == 'versicolor'
df2 = df['species'] == 'virginica'

petal_length_media_setosa = round(df[df0]['petal_length'].mean(), 2)
petal_length_media_versicolor = df[df1]['petal_length'].mean()
petal_length_media_virginica = round(df[df2]['petal_length'].mean(), 2)

print(petal_length_media_setosa)
print(petal_length_media_versicolor)
print(petal_length_media_virginica)
