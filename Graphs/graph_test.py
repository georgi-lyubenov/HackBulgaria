import unittest
import graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = graph.DirectedGraph()

    def test_print(self):
        self.assertEqual(self.graph.to_string(), "{}")

    def test_add(self):
        self.graph.add_edge(1, 2)
        self.assertEqual(self.graph.to_string(), "{1: 2}")

    def test_neightbours(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(5, 1)
        self.assertEqual(self.graph.getNeighboursFor(1), "[3, 5]")

    def test_path(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(5, 1)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(3, 5)
        self.assertTrue(self.graph.path_between(3, 2))
        self.assertFalse(self.graph.path_between(5, 3))

if __name__ == '__main__':
    unittest.main()
