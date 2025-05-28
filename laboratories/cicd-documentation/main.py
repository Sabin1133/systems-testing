from tree import Tree
from node import Node

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()


def test_first():
    assert tree._find(3, tree.getRoot())


def test_second():
    assert tree._find(5, tree.getRoot())


if __name__ == "__main__":
    pass
