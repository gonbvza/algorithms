from algorithms.graph import find_path
import unittest

class TestSinglePath(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['E', 'F'],
            'D': [],
            'E': ['B', 'D'],
            'F': []
        }

        self.graph_without_neighbours = {
            'A': [],
        }

    def test_find_single_path(self):
        single_path = find_path.find_path(self.graph, 'A', 'D', {})
        self.assertEqual(['A', 'B', 'D'], single_path)

    def test_no_start(self):
        self.assertIsNone(find_path.find_path(self.graph, '', 'D', {}))

    def test_start_without_neighbours(self):
        self.assertIsNone(find_path.find_path(self.graph_without_neighbours, 'A', 'D', {}))

class TestFindAllPaths(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['E', 'F'],
            'D': [],
            'E': ['B', 'D'],
            'F': []
        }

    def test_no_start(self):
        self.assertEqual(find_path.find_all_path(self.graph, '', 'D', {}), [])

class TestFindShortestPath(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': ['F'],
            'E': ['F'],
            'F': []
        }

    def test_shortest(self):
        shortest_path = find_path.find_shortest_path(self.graph, 'A', 'F', {})
        self.assertEqual(shortest_path, ['A', 'C', 'F'])

    def test_no_start(self):
        self.assertIsNone(find_path.find_shortest_path(self.graph, '', 'D', {}), [])

if __name__ == '__main__':
    unittest.main()

