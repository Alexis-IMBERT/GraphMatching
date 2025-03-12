"""This module test FUGW_barycenter implemntation

.. moduleauthor:: Marius Thorre
"""

import os

from unittest import TestCase
import graph_matching.algorithms.barycenter.fugw_barycenter as fugw_barycenter
from graph_matching.utils.graph_processing import get_graph_from_pickle

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
graph_test_path = os.path.join(
    project_root, "resources/graph_for_test/generation/without_outliers/noise_60"
)
graphs = []
for g in os.listdir(graph_test_path):
    graphs.append(get_graph_from_pickle(os.path.join(graph_test_path, g)))


class TestFUGW_barycenter(TestCase):
    def test_compute(self):
        F_b, _ = fugw_barycenter.compute(graphs=graphs, rho=1, epsilon=0.01, alpha=0.35)

        # tmp = nx.Graph()
        # for node, i in enumerate(F_b):
        #     tmp.add_node(node, coord=i, label=0)
        #     print(node, i)
        #
        # v = Visualisation(
        #     graph=tmp,
        #     sphere_radius=100,
        #     title="181 without outliers"
        # )
        # v.plot_graphs(folder_path=graph_test_path)
