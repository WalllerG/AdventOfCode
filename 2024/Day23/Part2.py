from collections import defaultdict
from Util.util import read_input
import networkx as nx

data = read_input(23,True)

cache = defaultdict(list)
for line in data:
    l, r = line.split("-")
    cache[l].append(r)
    cache[r].append(l)

G = nx.Graph(cache)
complete_g = list(nx.find_cliques(G))

ans = max(complete_g, key=len)
print(",".join(sorted(ans)))






