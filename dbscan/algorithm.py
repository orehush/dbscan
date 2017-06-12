import importlib

import numpy as np

from .const import UNCLASSIFIED, NOISE

__all_ = ('DBSCAN', )


class DBSCAN(object):
    def __init__(self, eps: float, min_points: int, distance='euclidean'):
        """

        Implementation of Density Based Spatial Clustering
            of Applications with Noise

        See https://en.wikipedia.org/wiki/DBSCAN

        :param eps - Maximum distance two points can be to be regionally related
        :param min_points - The minimum number of points to make a cluster
        :param distance - 'euclidean' or 'manhattan' or callable

        """
        self.eps = eps
        self.min_points = min_points
        self.distance_func = self._get_distance_function(distance)

    @staticmethod
    def _get_distance_function(distance):
        if callable(distance):
            distance_func = distance
        else:
            dbscan_module = importlib.import_module('dbscan')
            distance_func = getattr(dbscan_module, distance, None)
            if distance_func is None:
                raise ValueError("%s not supported distance" % distance)
        return distance_func

    def _eps_neighborhood(self, x: np.ndarray, y: np.ndarray) -> bool:
        return self.distance_func(x, y) < self.eps

    def _region_query(self, data: np.ndarray, point_id: int) -> list:
        n_points = data.shape[1]
        seeds = []
        for i in range(0, n_points):
            if self._eps_neighborhood(data[:, point_id], data[:, i]):
                seeds.append(i)
        return seeds

    def _expand_cluster(self, data: np.ndarray, classifications: list,
                        point_id: int, cluster_id: int) -> bool:

        seeds = self._region_query(data, point_id)
        if len(seeds) < self.min_points:
            classifications[point_id] = NOISE
            return False

        classifications[point_id] = cluster_id
        for seed_id in seeds:
            classifications[seed_id] = cluster_id

        while len(seeds) > 0:
            current_point = seeds[0]
            results = self._region_query(data, current_point)
            if len(results) >= self.min_points:
                for point in results:
                    if classifications[point] not in [UNCLASSIFIED, NOISE]:
                        continue

                    if classifications[point] == UNCLASSIFIED:
                        seeds.append(point)

                    classifications[point] = cluster_id
            seeds = seeds[1:]
        return True

    def fit(self, data: np.ndarray) -> list:
        """
        Inputs:
        :param data: A matrix whose columns are feature vectors
        Outputs:
        :return An list with either a cluster id number or NOISE (-1)
        for each column vector in m.
        """

        cluster_id = 0
        cnt_points = data.shape[1]
        classifications = [UNCLASSIFIED] * cnt_points
        for point_id in range(0, cnt_points):
            if classifications[point_id] != UNCLASSIFIED:
                continue
            if self._expand_cluster(data, classifications, point_id,
                                    cluster_id):
                cluster_id += 1
        return classifications
