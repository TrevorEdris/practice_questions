class RateGraph():
    def __init__(self, rates):
        """
        Initialize the graph from an iterable of (start, end, rate) tuples
        """
        self.graph = {}
        for orig, dest, rate in rates:
            self.add_conversion(orig, dest, rate)

    def add_conversion(self, orig, dest, rate):
        """
        Insert a conversion into the graph
        """
        if orig not in self.graph:
            self.graph[orig] = {}
        self.graph[orig][dest] = rate

        # If we know inch --> foot then we know foot --> inch
        if dest not in self.graph:
            self.graph[dest] = {}
        self.graph[dest][orig] = 1.0 / rate

    def get_neighbors(self, node):
        """
        Returns an iterable of the nodes neighboring the given node
        """
        if node not in self.graph:
            return None
        return self.graph[node].items()

    def get_nodes(self):
        """
        Returns an iterable of all nodes in the graph
        """
        return self.graph.keys()

    def get_graph(self):
        """
        Returns the graph itself
        """
        return self.graph