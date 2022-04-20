import rhino3dm as rg
import random as ra
import networkx as nx

def createGraph(n):
    ''' Takes one integer and one float to create a random graph

    Parameters
    -------------
    n = order of the graph
    '''

    G = nx.binomial_tree(n)
    #print(G.edges.data())
    
    return G



def addWeights(G,w):
    NG = nx.Graph()
    weights = {}
    for i in G.edges:
        weights[i] = ra.randint(1,w)
    #print(weights)
    nx.set_edge_attributes(G, values = weights, name = 'weight')
    #print(G.edges.data())
    #nx.draw(G)
    #plt.show()
    #print(type(G))
    return G

def getNodes(G, layout = 0):
    lay_all = (nx.kamada_kawai_layout(G), nx.circular_layout(G), nx.shell_layout(G), nx.spiral_layout(G), nx.planar_layout(G))
    lay = lay_all[layout]
    #print(lay.values())
    nodes = [rg.Point3d( d[0], d[1] , 0) for d in lay.values()]
    #print(type(nodes))
    return nodes

def getEdges(G, layout = 0):
    lay_all = (nx.kamada_kawai_layout(G), nx.circular_layout(G), nx.shell_layout(G), nx.spiral_layout(G), nx.planar_layout(G))
    lay = lay_all[layout]

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    #print(edges)
    return edges



r= createGraph(5)
s = addWeights(r,50)
t = getNodes(s, 0)
u = getEdges(s,0)