#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

import numpy as np
from sklearn.cluster import DBSCAN as skDBSCAN

from dbscan import DBSCAN


class TestDBSCANMethod(TestCase):

    def setUp(self):
        self.data = np.matrix('1   1.2 0.8 3.7 3.9 3.6 10;'
                              '1.1 0.8 1   4   3.9 4.1 10')
        self.eps = 0.55
        self.min_points = 2

    def test_dbscan(self):
        dbscan = DBSCAN(self.eps, self.min_points)
        self.assertListEqual(
            dbscan.fit(self.data),
            [0, 0, 0, 1, 1, 1, -1]
        )

    def test_compare_with_sklearn(self):
        dbscan = DBSCAN(self.eps, self.min_points)
        self.assertListEqual(
            dbscan.fit(self.data),
            list(skDBSCAN(self.eps, self.min_points).fit_predict(self.data.T))
        )

    def test_compare_with_sklearn_manhattan_metrics(self):
        dbscan = DBSCAN(self.eps, self.min_points, distance='manhattan')
        self.assertListEqual(
            dbscan.fit(self.data),
            list(skDBSCAN(self.eps, self.min_points, 'manhattan').fit_predict(
                self.data.T))
        )
