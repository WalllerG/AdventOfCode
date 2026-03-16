from collections import defaultdict
import networkx as nx
from Util.util import read_input
data = read_input(True)

components = defaultdict(list)
for line in data:
    name, targets = line.split(": ")
    for target in targets.split(" "):
        components[target].append(name)
        components[name].append(target)

graph = nx.Graph(components)
cur_v, partitions = nx.stoer_wagner(graph)
print(len(partitions[0]) * len(partitions[1]))



