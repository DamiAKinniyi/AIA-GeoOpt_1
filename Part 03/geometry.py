from re import X
import rhino3dm as rg
import random as ra
import math
import networkx as nx

def getnetworkX(points, curves):
    G = nx.Graph()
    G.add_nodes_from(points)
    #pointsX = [(point.X, point.Y, point.Z) for point in points]

    edge_points = []
    for edge in curves:
        u = points.index(edge.PointAtStart)
        v = points.index(edge.PointAtEnd)
        edge_points.append((u,v))

    G.add_edges_from(edge_points)

def getnetworkx(points, curves):
    G = nx.Graph()
    G.add_nodes_from(points)
    #pointsX = [(point.X, point.Y, point.Z) for point in points]

    edge_points = []
    for edge in curves:
        u = points.index(edge.PointAtStart)
        v = points.index(edge.PointAtEnd)
        edge_points.append((u,v))

    G.add_edges_from(edge_points)

    return G



