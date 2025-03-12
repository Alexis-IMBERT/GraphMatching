"""This module contains sphere_sampling.py test
..moduleauthor:: Marius THORRE
"""

import graph_matching.algorithms.graph_generation.sphere_sampling as sphere_sampling
from unittest import TestCase
import numpy as np


class TestSphereSampling(TestCase):
    def test_fibonacci(self):
        x, y, z = sphere_sampling.fibonacci(nb_point=6, radius=100)
        x_truth = np.array(
            [
                55.27707984,
                -63.85801804,
                8.62029271,
                59.99288074,
                -85.27868937,
                46.6403288,
            ]
        )
        y_truth = np.array(
            [-83.33333333, -50.0, -16.66666667, 16.66666667, 50.0, 83.33333333]
        )
        z_truth = np.array(
            [0.0, 58.49917548, -98.22378926, 78.25008934, -15.08459939, -29.66875942]
        )

        self.assertTrue(np.allclose(x, x_truth))
        self.assertTrue(np.allclose(y, y_truth))
        self.assertTrue(np.allclose(z, z_truth))
