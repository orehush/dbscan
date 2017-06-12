======
dbscan
======


Density-based spatial clustering of applications with noise (DBSCAN)


Description
===========
Density-based spatial clustering of applications with noise (DBSCAN)
is a data clustering algorithm proposed by Martin Ester, Hans-Peter Kriegel,
Jörg Sander and Xiaowei Xu in 1996.[1] It is a density-based clustering algorithm:
given a set of points in some space, it groups together points that are closely
packed together (points with many nearby neighbors), marking as outliers points
that lie alone in low-density regions (whose nearest neighbors are too far away).
DBSCAN is one of the most common clustering algorithms and also most cited in scientific literature.[2]


Instalation
===========

pip install git+https://github.com/orehush/dbscan@v0.0.1


Simple usage
============

>>> import numpy as np
>>> from dbscan import DBSCAN, plot
>>> n, m = 2, 10
>>> data = np.random.rand(n, m)
>>> eps, min_points = 0.5, 3
>>> dbscan = DBSCAN(eps, min_points)
>>> labels = dbscan.fit(data)
>>> print(labels)
>>> plot(data, labels)


Note
====

1. Ester, Martin; Kriegel, Hans-Peter; Sander, Jörg; Xu, Xiaowei (1996). Simoudis, Evangelos; Han, Jiawei; Fayyad, Usama M., eds. A density-based algorithm for discovering clusters in large spatial databases with noise. Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96). AAAI Press. pp. 226–231. CiteSeerX 10.1.1.121.9220 Freely accessible. ISBN 1-57735-004-9.
2. Most cited data mining articles according to Microsoft academic search; DBSCAN is on rank 24, when accessed on: 4/18/2010
