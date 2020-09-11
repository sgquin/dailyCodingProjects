import unittest 
from unival import *

class TestCount(unittest.TestCase):
    def test_unival(self):
        node1 = Node(1,'node1')
        node2 = Node(1,'node2')
        node3 = Node(1, 'node3', node1, node2)
        node4 = Node(0,'node4')
        node5 = Node(1,'node5')
        node6 = Node(0,'node6', node3, node4)
        node7 = Node(0, 'node7', node5, node6)
        count = numberUnivalAtOrBelow(node7)
        countExp = 5
        self.assertEqual(count,countExp)

    def test_descendents(self):
        node1 = Node(1,'node1')
        node2 = Node(1,'node2')
        node3 = Node(1, 'node3', node1, node2)
        node4 = Node(0,'node4')
        node5 = Node(1,'node5')
        node6 = Node(0,'node6', node3, node4)
        node7 = Node(0, 'node7', node5, node6)
        self.assertTrue(areDescendentsEqual(node1))
        self.assertTrue(areDescendentsEqual(node2))
        self.assertTrue(areDescendentsEqual(node3))
        self.assertTrue(areDescendentsEqual(node4))
        self.assertTrue(areDescendentsEqual(node5))
        self.assertFalse(areDescendentsEqual(node6))
        self.assertFalse(areDescendentsEqual(node7))

if __name__ == "__main__":
    unittest.main()
