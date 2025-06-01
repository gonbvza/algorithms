from find_path import *

find_path_coverage = {
        "start_is_end": False,
        "no_start": False,
        "no_node": False,
        "no_graph": False
}

find_all_path_coverage = {
        "start_is_end": False,
        "no_start": False,
        "no_node": False,
}

find_shortest_path_coverage = {
        "start_is_end": False,
        "no_start": False,
        "no_node": False,
        "newpath": False,
        "found_shortest": False
}

def print_coverage(coverage_keys):
    for key, value in coverage_keys.items():
        print(f"The branch {key}: {value}")

def main():
    # Define the variables of the graph
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E', 'F'],
        'D': [],
        'E': ['B', 'D'],
        'F': []
    }

    graph_with_no_neighbour = {
        'A': [],
    }


    print("Coverage for the function find_path")
    # Normal case
    find_path(graph, 'A', 'D', find_path_coverage, [])
    print_coverage(find_path_coverage)
   
    print()

    # No start case
    find_path(graph, '', 'D', find_path_coverage, [])
    print_coverage(find_path_coverage)
    
    print()

    # No graph case
    find_path(graph_with_no_neighbour, 'A', '', find_path_coverage, [])
    print_coverage(find_path_coverage)


    print()

    print("Coverage for the function find_all_path")
    # Normal case
    find_all_path(graph, 'A', 'D', find_all_path_coverage, [])
    print_coverage(find_all_path_coverage)
    
    print()

    # Normal case
    find_all_path(graph, '', 'D', find_all_path_coverage, [])
    print_coverage(find_all_path_coverage)
    
    print()

    print("Coverage for the function find_shortest_path_path")
    # Normal case
    find_shortest_path(graph, 'A', 'D', find_shortest_path_coverage, [])
    print_coverage(find_shortest_path_coverage)
    
    print()

    # Normal case
    find_all_path(graph, '', 'D', find_shortest_path_coverage, [])
    print_coverage(find_shortest_path_coverage)

if __name__ == "__main__":
    main()

