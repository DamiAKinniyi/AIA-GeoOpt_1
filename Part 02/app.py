from flask import Flask
import ghhops_server as hs
import geometry as geo


app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/binomialGraph",
    name = 'Binomial_Graph',
    inputs = [
        hs.HopsInteger('Order', 'O' , "Set order of the graph", hs.HopsParamAccess.ITEM, default=3),
        hs.HopsInteger('Weight', 'W', "Set edge weights", hs.HopsParamAccess.ITEM, default=5),
        hs.HopsInteger('Layout', 'L', "Select layout type from 0 to 4", hs.HopsParamAccess.ITEM, default=3)
    ],
    outputs = [
        hs.HopsPoint('Nodes', 'N', 'Output points', hs.HopsParamAccess.LIST),
        hs.HopsCurve('Edges', 'E', 'Output curves', hs.HopsParamAccess.LIST)
    ]
)

def create(o,w,l):
    G = geo.createGraph(o)
    GW = geo.addWeights(G,w)

    nodes = geo.getNodes(GW, l)
    edges = geo.getEdges(GW, l)
    return nodes, edges


if __name__== "__main__":
    app.run(debug=True)
