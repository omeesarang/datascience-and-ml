from sklearn import tree 
X = [[185,66,9],[176,54,7],[180,88,9],[160,55,7],[140,87,5],[144,45,4]]
Y = ['man','woman','man','woman','child','child']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)
prediction = clf.predict([[155,60,8]])
print(prediction)