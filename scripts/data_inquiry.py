import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("the_dataaaa.csv")

# Proccess data
df[["Home Team Wins"]] *= 1
df.rename(columns={'Home Team Wins':'HOME_TEAM_WINS'}, inplace=True)
df[['HOME_TEAM_WINS']] = df[['HOME_TEAM_WINS']].astype(float)


corrmat = df.corr()
# f, ax = plt.subplots(figsize=(20,18))
# sns.heatmap(corrmat, vmax=.8, square=True)
# plt.show()

#team result

k = 9
cols = corrmat.nlargest(k, "HOME_TEAM_WINS")["HOME_TEAM_WINS"].index
f, ax = plt.subplots(figsize=(10,6))
cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
