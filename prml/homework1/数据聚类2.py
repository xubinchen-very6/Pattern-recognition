import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.ensemble import GradientBoostingClassifier
import time

data=pd.read_csv('/Users/macbookair/PycharmProjects/PR/homework1/julei2.txt',delimiter=' ')
data=data.values
x=data[:,0]
y=data[:,1]

time_start=time.time()
db=DBSCAN(eps=7.071,min_samples=113)
label=db.fit_predict(data)

x_db=x[label != -1]
x_noise=x[label == -1]
y_db=y[label != -1]
data_db=data[label != -1]
data_noise=data[label == -1]
y_noise=y[label == -1]
label_db=label[label != -1]
label_noise=label[label == -1]

gbdt=GradientBoostingClassifier(n_estimators=150,learning_rate=0.06,subsample=0.6)
gbdt.fit(data_db,label_db)
label_new=gbdt.predict(data_noise)
time_end = time.time()


plt.figure(figsize=(12,7))
plt.subplot(141)
plt.title(r'$Raw$$Data$')
plt.scatter(x,y,s=2)
plt.subplot(142)
plt.title(r'$DBSCAN+Remove$ $noise$')
plt.scatter(x_db,y_db,c=label_db,s=2)
plt.subplot(144)
plt.title(r'$DBSCAN+GBDT$')
plt.scatter(x_db,y_db,c=label_db,s=2)
plt.scatter(x_noise,y_noise,c=label_new,s=2)
plt.subplot(143)
plt.title(r'$noise$')

plt.scatter(data_noise[:,0],data_noise[:,1],c=label_new,s=2)




plt.tight_layout()
plt.savefig('homework2')

print(time_end-time_start)
plt.show()
