import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph() #A new (empty) undirected graph
g.add_node("Alan") #Add one new node
g.add_nodes_from(["Bob","Carol","Denise"])#Add three new nodes from list
#Nodes can have attributes

g.node["Alan"]["gender"]="M"
g.node["Bob"]["gender"]="M"
g.node["Carol"]["gender"]="F"
g.node["Denise"]["gender"]="F"

for n in g:
	print("{0} has gender {1}".format(n,g.node[n]["gender"]))

g.add_edge("Alan","Bob") #Add one new edge
#Add two new edges
g.add_edges_from([["Carol","Denise"],["Carol","Bob"]])
#Edge attributes
g.edge["Alan"]["Bob"]["relationship"] = "Friends"
g.edge["Carol"]["Denise"]["relationship"] = "Friends"
g.edge["Carol"]["Bob"]["relationship"] = "Married"

#New edge with an attribute
g.add_edges_from([["Carol","Alan",
{"relationship":"Friends"}]])

for e in g.edges_iter():
	n1=e[0]
	n2=e[1]
	print("{0} and {1} are {2}".format(n1,n2,g.edge[n1][n2]["relationship"]))

#Save g to the file my_graph.graphml in graphml format
#prettyprint will make it nice for a human to read
nx.write_graphml(g,"my_graph.graphml",prettyprint=True)
#Layout g with the Fruchterman-Reingold force-directed
#algorithm and save the result to networkx_graph.png
#with_labels will label each node with its id

nx.draw_spring(g,with_labels=True)
plt.savefig("networkx_graph.png")
plt.clf() #Clear plot

print 'Information about the graph'
print nx.info(g)
#print g.number_of_nodes()
print g.nodes(data=True)
#print g.number_of_edges()
print g.edges(data=True)
print 'Average degree of nodes'
print nx.density(g)
print "\n"
print 'Number of connected components'
print nx.number_connected_components(g)
print "\n"
print "Printing all shortest paths"
print nx.all_pairs_shortest_path(g)
print "\n"
print 'Betweeness Centrality'
print nx.betweenness_centrality(g)
print "\n"
print 'Clustering coefficients'
print nx.clustering(g)
print nx.clustering(g, nodes=["Bob"])

