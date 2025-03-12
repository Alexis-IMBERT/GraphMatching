"""This module contains tools to generate barycenter graph from graph list
..Moduleauthor:: Marius Thorre
"""

from pathlib import Path
from graph_matching.utils.display_graph_tools import Visualisation
from graph_matching.algorithms.barycenter.fgw_barycenter import Barycenter
from graph_matching.utils.graph_processing import get_graph_from_pickle

graph_test_path = Path(__file__).resolve().parent.parent / "resources/graph_for_test"
file_cortex_mesh = (
    Path(__file__).resolve().parent.parent
    / "resources/template_mesh/lh.OASIS_testGrp_average_inflated.gii"
)
file_sphere_mesh = (
    Path(__file__).resolve().parent.parent / "resources/template_mesh/ico100_7.gii"
)

# generation graph path with a little noise
graph_test_path = (
    Path(__file__).resolve().parent.parent
    / "resources/graph_for_test/generation/without_outliers/noise_60"
)
# extract pickle graph file in networkx graph
graphs = [get_graph_from_pickle(graph_test_path / g) for g in graph_test_path.iterdir()]

# compute barycenter graph
b = Barycenter(graphs=graphs, nb_node=30)
print("Starting barycenter computation, please hold on ...")
b.compute()

bary = b.get_graph()

# visualise barycenter graph in an html web page
v = Visualisation(graph=bary, sphere_radius=100, title="1 without outliers")

# add all graphs used for barycenter generation on web page
v.plot_graphs(folder_path=graph_test_path)
# Barycenter is going to be 'Trace 0', you can click on it to see where is it
v.show_fig()
