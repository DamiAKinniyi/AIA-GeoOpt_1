from flask import Flask
import ghhops_server as hs
import geometry as geo
import networkx as nx
import matplotlib.pyplot as plt


app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/proximityGraph",
    name = 'Binomial_Graph',
    inputs = [
        hs.HopsPoint('Nodes', 'N', 'Output points', hs.HopsParamAccess.LIST),
        hs.HopsCurve('Edges', 'E', 'Output curves', hs.HopsParamAccess.LIST)
    
    ]
)

def create(points, curves):
    G = geo.getnetworkx(points, curves)
    nx.draw(G)
    plt.show()

if __name__== "__main__":
    app.run(debug=True)

