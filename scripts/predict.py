import pandas as pd
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import graphviz
from sklearn import tree


# Prepare data
df = pd.read_csv("the_dataaaa.csv")
df[["Home Team Wins"]] *= 1
df.rename(columns={'Home Team Wins':'HOME_TEAM_WINS'}, inplace=True)
df[['HOME_TEAM_WINS']] = df[['HOME_TEAM_WINS']].astype(float)

#prepare x and y

# feature_cols = ['opptPTS', 'teamDrtg', 'teamPF', 'teamTO', 'teamORB', 'teamFGA']
feature_cols = ['HOME_W_PCT', 'HOME_FG_PCT', 'HOME_FG3_PCT', 'HOME_OREB', 'HOME_DREB', 'HOME_AST', 'HOME_TOV', 'HOME_STL', 'HOME_BLK', 'HOME_PTS', 'AWAY_DATE', 'AWAY_W_PCT', 'AWAY_FG_PCT', 'AWAY_FG3_PCT', 'AWAY_OREB','AWAY_DREB', 'AWAY_AST', 'AWAY_TOV', 'AWAY_STL', 'AWAY_BLK', 'AWAY_PTS']
x = df[feature_cols]
y = df['HOME_TEAM_WINS']
# print(x.head())


#train test split, standardize data

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.4, random_state=2)

#knn

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
pred = knn.predict(x_test)
# print(metrics.accuracy_score(y_test, pred))
print(knn.predict_proba(x_test))


#linear svm

clf = LinearSVC(random_state=2)
clf.fit(x_train, y_train)
print(clf.coef_)
print(clf.intercept_)
pred = (clf.predict(x_test))
print(metrics.accuracy_score(y_test, pred))


#random forrest classifier

clf = RandomForestClassifier()
clf.fit(x_train, y_train)
print(clf.feature_importances_)
pred = clf.predict(x_test)
print(metrics.accuracy_score(y_test, pred))

# Gradient Treee Boosting

clfgtb = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(x_train, y_train)
clfgtb.score(x_test, y_test)
