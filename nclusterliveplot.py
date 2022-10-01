import random as rd
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    pass

SIZE = 20
RANGE_START = 1
RANGE_END = 100
K = 3


class Cluster:
    def __init__(self, k, iteration=10,k_lim = 2):
        self.finalX = []
        self.finalY = []
        self.iter_X = []
        self.iter_Y = []
        self.k = k
        self.k_lim = k_lim
        self.set_j_x = []
        self.set_j_y = []
        self.initLivePlot = False
        self.iteration = iteration
        self.centroids = [[rd.randint(0, 100), rd.randint(0, 100)] for i in range(self.k)]
        self.initcluster()


    def initPlot(self):
        plt.ion()
        colors = ['blue', 'red', 'green']
        self.figure, ax = plt.subplots(figsize=[10, 10])
        plt.xlim(0, 100)
        plt.ylim(0, 100)

        self.catplot1 = ax.plot(self.clustersX[0], self.clustersY[0], 'o', color=colors[0])[0]
        self.catplot2 = ax.plot(self.clustersX[1], self.clustersY[1], 'o', color=colors[1])[0]
        self.catplot3 = ax.plot(self.clustersX[2], self.clustersY[2], 'o', color=colors[2])[0]

        self.centroidplot1 = ax.plot(self.centroids[0][0],self.centroids[0][1], 'p', markersize=15, color='blue', markeredgecolor="blue")[0]
        self.centroidplot2 = ax.plot(self.centroids[1][0],self.centroids[1][1], 'p', markersize=15, color='red', markeredgecolor="blue")[0]
        self.centroidplot3 = ax.plot(self.centroids[2][0],self.centroids[2][1], 'p', markersize=15, color='green', markeredgecolor="blue")[0]

    def initcluster(self):
        self.clustersX = [[] for i in range(self.k)]
        self.clustersY = [[] for i in range(self.k)]

    def distance(self, cent, point):
        return ((cent[0] - point[0]) ** 2 + (cent[1] - point[1]) ** 2) ** 0.5

    def plotCluster(self):
        for i in range(self.k):
            plt.scatter(self.finalX[i], self.finalY[i])
        plt.show()

    def livePlot(self):
        self.catplot1.set_xdata(self.clustersX[0])
        self.catplot1.set_ydata(self.clustersY[0])
        self.catplot2.set_xdata(self.clustersX[1])
        self.catplot2.set_ydata(self.clustersY[1])
        self.catplot3.set_xdata(self.clustersX[2])
        self.catplot3.set_ydata(self.clustersY[2])

        self.centroidplot1.set_xdata(self.centroids[0][0])
        self.centroidplot1.set_ydata(self.centroids[0][1])

        self.centroidplot2.set_xdata(self.centroids[1][0])
        self.centroidplot2.set_ydata(self.centroids[1][1])

        self.centroidplot3.set_xdata(self.centroids[2][0])
        self.centroidplot3.set_ydata(self.centroids[2][1])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        time.sleep(1)

    def avgCentroid(self):
        for clust in range(self.k):
            new_centX = 0
            new_centY = 0
            for cent in range(len(self.clustersX[clust])):
                new_centX += self.clustersX[clust][cent]
                new_centY += self.clustersY[clust][cent]
            try:
                self.centroids[clust][0] = new_centX / len(self.clustersX[clust])
                self.centroids[clust][1] = new_centY / len(self.clustersY[clust])
            except ZeroDivisionError:
                self.centroids[clust][0] = -1
                self.centroids[clust][1] = -1

    def costJ(self):
        costvalueX = 0
        costvalueY = 0
        for cent in range(self.k):
            jx = 0
            jy = 0
            for centpoint in range(len(self.finalX[cent])):
                jx += (self.finalX[cent][centpoint]-self.centroids[cent][0])**2
                jy += (self.finalY[cent][centpoint] - self.centroids[cent][1]) ** 2
            costvalueX += jx / len(self.finalX[cent])
            costvalueY += jy / len(self.finalY[cent])

        self.set_j_x.append([self.finalX,costvalueX])
        self.set_j_x.append([self.finalY,costvalueY])

    def optimize(self):
        for iter in range(self.iteration):
            self.initcluster()
            for i in range(len(self.iter_X)):
                point = [self.iter_X[i], self.iter_Y[i]]
                selected_centroid = 0
                mindis = self.distance(self.centroids[0], point)
                for j in range(self.k):
                    dis = self.distance(self.centroids[j], point)
                    if mindis > dis:
                        mindis = dis
                        selected_centroid = j
                self.clustersX[selected_centroid].append(point[0])
                self.clustersY[selected_centroid].append(point[1])
            self.avgCentroid()
            self.livePlot()

    def fit(self, x, y):
        self.iter_X = x
        self.iter_Y = y
        self.initPlot()
        self.optimize()
        self.finalX = self.clustersX
        self.finalY = self.clustersY
        self.costJ()
        # for k in range(2,self.k_lim+1):
        #     self.iter_X = x
        #     self.iter_Y = y
        #     self.initPlot()
        #     self.optimize()
        #     self.k = k
        #     self.finalX = self.clustersX
        #     self.finalY = self.clustersY
        #     self.costJ()
        # print(self.set_j_x)


c = Cluster(K)

X = [rd.randint(RANGE_START, RANGE_END) for i in range(SIZE)]
Y = [rd.randint(RANGE_START, RANGE_END) for i in range(SIZE)]

c.fit(X, Y)
c.plotCluster()
