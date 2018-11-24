import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


df=pd.read_csv('diabetes.csv')


X=df.values[:,0:-1]
y=df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)


clf1=RandomForestClassifier()
clf1.fit(X_train,y_train)


z=accuracy_score(y_test,clf1.predict(X_test))

print(f'accuracy on 20% testing set is {z}')
dia = pickle.dumps(clf)
joblib.dump(clf1, 'dia.joblib')
print('model saved')



