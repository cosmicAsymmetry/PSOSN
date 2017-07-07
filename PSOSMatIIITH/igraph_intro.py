import igraph
from igraph import *

# load data into a graph
g = igraph.Graph.Read_Ncol('connections.txt')
print g.summary()
print 'Average Path Length'
print g.average_path_length()
print 'Edge between-ness'
print g.edge_betweenness()

print 'Selecting degree with multiple vertices'
print [v.index for v in g.vs.select(_degree = g.maxdegree())]

print "Clusters in the graph"
print g.components()

c = g.community_edge_betweenness()
m = c.as_clustering()
print m
for i in m.subgraphs():
    for j in i.vs:
        print j['name'],
    print  " "