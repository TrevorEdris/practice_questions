from collections import deque


def bfs(graph, start, end):
    to_visit = deque()
    to_visit.appendleft( (start, 1.0) )
    visited = set()

    while to_visit:
        node, rate_from_origin = to_visit.pop()
        if node == end:
            return True
        visited.add(node)
        for unit, rate in graph.get_neighbors(node):
            if unit not in visited:
                to_visit.append((unit, rate_from_origin * rate))

    return None


def make_conversions(graph):
    def conversions_bfs(rate_graph, start, conversions):
        to_visit = deque()
        to_visit.appendleft( (start, 1.0) )

        while to_visit:
            node, rate_from_origin = to_visit.pop()
            conversions[node] = (start, rate_from_origin)
            for unit, rate in rate_graph.get_neighbors(node):
                if unit not in conversions:
                    to_visit.append( (unit, rate_from_origin * rate) )

        return conversions

    conversions = {}
    for node in graph.get_nodes():
        if node not in conversions:
            conversions_bfs(graph, node, conversions)

    return conversions