from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import time
from sklearn.cluster import DBSCAN
data=pd.read_csv('/Users/macbookair/PycharmProjects/PR/homework1/julei1.txt',delimiter=' ')
data=data.values
x=data[:,0]
y=data[:,1]
time_start=time.time()
km=KMeans(n_clusters=2)
label=km.fit_predict(data)
plt.subplot(121)
plt.title(r'$Raw data$')
plt.scatter(x,y,s=2)
plt.subplot(122)
plt.title(r'$KMeans$')
plt.scatter(x,y,c=label,s=2)
plt.scatter(km.cluster_centers_[0][0],km.cluster_centers_[0][1],c='red',marker='*',s=30,label='cluster center1')
plt.scatter(km.cluster_centers_[1][0],km.cluster_centers_[1][1],c='red',marker='*',s=30,label='cluster center2')
plt.legend()
plt.savefig('homework1')
time_end=time.time()
print(time_end-time_start)
# dbc= DBSCAN(eps=17,min_samples = 440)
# label1 = dbc.fit_predict(data)
# plt.subplot(121)
# plt.title(r'$Raw data$')
# plt.scatter(x,y,s=2)
# plt.subplot(122)
# plt.title(r'$KMeans$')
# plt.scatter(x,y,c=label1,s=2)
# plt.legend()
#

plt.show()
