class graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # create an undirected graph
    # this is done by creating symetric edges
    def make_undirected(self):
        for item in list(self.graph_dict.keys()):
            for(b, dist) in self.graph_dict[item].items():
                self.graph_dict.setdefault(b, {})[item] = dist

    # add a link between nodes A and B of a given distance
    # this will create an inverse link assuming the graph is undirected
    def connect(self, node_a, node_b, distance = 1):
        self.graph_dict.setdefault(node_a, {})[node_b] = distance
        if not self.directed:
            self.graph_dict.setdefault(node_b, {})[node_a] = distance

    # get the neighbor(s) of the current node
    def get(self, node_a, node_b = None):
        links = self.graph_dict.setdefault(node_a, {})
        if node_b is None:
            return links
        else:
            return links.get(node_b)

    # get a list of nodes in the graph
    def node_list(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)