import numpy as np
import pandas as pd
from sklearn.externals import joblib

clf=joblib.load('dia.joblib')

l=[]

print('enter details')
for i in range(8):
    l.append(float(input('')))

x=np.array(l).reshape(-1,8)

pred=clf.predict(x)

if a==1:
    print('Sorry , kasht hai')
else:
    print('sorry, boht zyada kasht hai')


