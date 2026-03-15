import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins = os.path.dirname(__file__)
path = os.path.join(penguins, 'penguin.csv') if os.path.exists(os.path.join(penguins, 'penguin.csv')) else 'penguin.csv'
if not os.path.exists(path): print(f"CSV not found at {path}"); sys.exit(1)

df = pd.read_csv(path)
df.head(10)
df.shape
df.tail()
df.isnull().sum()
df.describe().T
df.describe()
df.dtypes
df.info()
df.isnull().sum()
df.describe(include="all")
df.corr()
sns.heatmap(df.corr(), cmap="Wistia", annot=True)
df.hist(figsize=(12, 8))
plt.show()
df.plot(kind="box", subplots=True, layout=(3, 2), sharex=False, sharey=False, figsize=(8, 12))
plt.show()
df.sex.value_counts()
df.island.value_counts()
df.species.value_counts()
sns.countplot(data=df, x="sex", palette="summer")
sns.countplot(data=df, x="island", palette="RdPu")
sns.countplot(data=df, x="species", palette="YlOrRd")
sns.countplot(data=df, x="sex", palette="rocket", hue="species")
sns.countplot(data=df, x="island", palette="husl", hue="species")
sns.countplot(data=df, x="island", hue="sex", palette="spring")
sns.pairplot(df, hue="species", palette="mako")
