import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

import pydotplus
from sklearn.externals.six import StringIO



#讀取資料
filename = open('winequality-red.csv', 'r')
file = pd.read_csv(filename, delimiter=";")
df = DataFrame(file)
df.head()

#定義品質高的紅酒等級為何
plt.hist(df["quality"])
plt.show()

#為使用CART 將品質7與8定義為1 其餘定義為0
new_quality = df["quality"].replace({7:1, 8:1, 6:0, 5:0, 4:0, 3:0})

drop_table = df.drop(df.columns[[-1]], axis=1)

new_df = drop_table.join(new_quality)

new_df.to_csv("test.csv")

#run CART

y = new_df.quality
x = drop_table

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4, min_samples_leaf=6)
clf = clf.fit(X_train, y_train)
print("準確率：{:.2f}".format(clf.score(X_test, y_test)))

#比較自變數重要程度
print(clf.feature_importances_)

#交叉驗證評估模型
score = cross_validation.cross_val_score(clf, x, y, cv=10)
print(score)

#畫出決策樹
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["fixed acidity","volatile acidity","citric acid",
                                                            "residual sugar","chlorides","free sulfur dioxide",
                                                            "total sulfur dioxide","density","pH","sulphates","alcohol",
                                                            ], class_names=["low_quality","high_quality"])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("wine.pdf")


#利用randomforest執行
#參考網站http://xccds1977.blogspot.tw/2014/10/python_26.html
clf2 = RandomForestClassifier(n_estimators=1500, random_state=50)
clf2 = clf2.fit(X_train, y_train)
score2  =cross_validation.cross_val_score(clf2, x, y, cv=10)
clf2.feature_importances_

print(score2.mean(),score.mean())