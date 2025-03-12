"""This module will contain test from graph_processing.py file
..moduleauthor:: Marius Thorre
"""

from pathlib import Path
import networkx as nx
from unittest import TestCase

from graph_matching.utils.graph_processing import get_graph_from_pickle

project_path = Path(__file__).resolve().parents[2]


class Test(TestCase):
    def test_get_graph_from_picle(self):
        g0_path = (
            project_path
            / "resources/graph_for_test/generation/without_outliers/noise_01/graph_00000.gpickle"
        )
        g0 = get_graph_from_pickle(g0_path)

        self.assertTrue(len(g0.nodes) == 30)
        self.assertTrue(type(g0) is nx.Graph)
