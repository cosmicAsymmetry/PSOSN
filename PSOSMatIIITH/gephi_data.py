import pandas as pd
import csv
import datetime

nodes = []
edges = []

def cout(message):
    print str(datetime.datetime.now()), ":", message
"""
csv_writer_nodes = csv.writer(open('nodes.csv', 'a'))
csv_writer_nodes.writerow(['ID','Label'])

csv_writer_edges = csv.writer(open('edges.csv', 'a'))
csv_writer_edges.writerow(['Source', 'Target', 'Weight'])

for i in xrange(200):
    csv_writer_nodes.writerow([i, i])
    csv_writer_edges.writerow([i, i+1, 1])

"""
#************************************CODE USING PANDAS****************************************
 for i in xrange(200):
     edges.append({'source': i, 'target': i+1, 'weight': 1})
     nodes.append({'id': i, 'label': i})

 edges = pd.DataFrame(edges) nodes = pd.DataFrame(nodes)

 print 'Printing nodes and edges now'
 cout(edges.info())
 cout(nodes.info())

 edges.to_csv('edges_pd.csv', index=False)
 nodes.to_csv('nodes_pd.csv', index=False)
