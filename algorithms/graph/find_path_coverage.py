from find_path import *

find_path_coverage = {
        "start_is_end": False,
        "no_start": False,
        "no_node": False,
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

    # Normal case
    find_path(graph, 'A', 'D', find_path_coverage, [])
    print_coverage(find_path_coverage)
    
    print()

    # No start case
    find_path(graph, '', 'D', find_path_coverage, [])
    print_coverage(find_path_coverage)
    

if __name__ == "__main__":
    main()

