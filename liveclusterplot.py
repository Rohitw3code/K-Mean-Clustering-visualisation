import random as rd
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
dset = iris.data[:, :2]

start = 0
end = 1000
size = 80
# size = len(dset)

def getRandom():
  return rd.randint(start,end)

# x = dset[:,0]
# y = dset[:,1]

x = [rd.randint(start,end) for m in range(size)]
y = [rd.randint(start,end) for n in range(size)]

c1 = [x[5],y[5]]
c2 = [x[7],y[7]]

catx1 , caty1 = [],[]
catx2 , caty2= [],[]

def findDis(x,y,c):
  return (((x-c[0])**2)+((y-c[1])**2))**0.5

plt.ion()
figure, ax = plt.subplots(figsize=[10,10])

plt.xlim(-end/10, end+end/4)
plt.ylim(-end/10, end+end/4)

plt.title("K-Mean Clustering", fontsize=20)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

catplot1, = ax.plot(catx1,caty1,'o',color='blue')
catplot2, = ax.plot(catx2,caty2,'o',color='green')

catplot3, = ax.plot(c1[0],c1[1],'p',markersize=15,color='red',markeredgecolor="blue")
catplot4, = ax.plot(c2[0],c2[1],'p',markersize=15,color='orange',markeredgecolor="green")

def cluster():
  global catx1,catx2,caty1,caty2,c1,c2
  sumx1,sumy1 = 0 , 0
  sumx2,sumy2 = 0 , 0
  for point in range(size):
    a,b = x[point],y[point]
    dist1 = findDis(a,b,c1)
    dist2 = findDis(a,b,c2)
    if dist1>dist2:
      catx2.append(a)
      caty2.append(b)
    else:
      catx1.append(a)
      caty1.append(b)

  for i in range(len(catx1)):
      sumx1 += catx1[i]
      sumy1 += caty1[i]

  for i in range(len(catx2)):
      sumx2 += catx2[i]
      sumy2 += caty2[i]

  c1 = [sumx1/len(catx1),sumy1/len(caty1)]
  c2 = [sumx2/len(catx2),sumy2/len(caty2)]

  catplot1.set_xdata(catx1)
  catplot1.set_ydata(caty1)

for _ in range(100):
    cluster()

    catplot1.set_xdata(catx1)
    catplot1.set_ydata(caty1)

    catplot2.set_xdata(catx2)
    catplot2.set_ydata(caty2)

    catplot3.set_xdata(c1[0])
    catplot3.set_ydata(c1[1])

    catplot4.set_xdata(c2[0])
    catplot4.set_ydata(c2[1])

    catx1, caty1 = [], []
    catx2, caty2 = [], []
    # drawing updated values
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.6)


if __name__ == "__main__":
    pass
