"""
Functions for finding paths in graphs.
"""

# pylint: disable=dangerous-default-value
def find_path(graph, start, end, coverage_keys, path=[]):
    """
    Find a path between two nodes using recursion and backtracking.
    """
    path = path + [start]
    if start == end:
        coverage_keys["start_is_end"] = True
        return path
    if not start in graph:
        coverage_keys["no_start"] = True
        return None
    for node in graph[start]:
        if node not in path:
            coverage_keys["no_node"] = True
            newpath = find_path(graph, node, end, coverage_keys, path)
            return newpath
    return None

# pylint: disable=dangerous-default-value
def find_all_path(graph, start, end, path=[]):
    """
    Find all paths between two nodes using recursion and backtracking
    """
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    """
    find the shortest path between two nodes
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
