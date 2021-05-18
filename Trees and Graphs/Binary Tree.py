# Binary Tree

# Each node has two or fewer children

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# When the tree has no gaps, the tree is considered "perfect"

# Perfect Tree Properties

# Property #1
# The number of total nodes on each level doubles moving down the tree

# Property #2
# The sum of the nodes on the bottom level is equal to the rest of the nodes + 1
# About half of the nodes are on the bottom level
# If we zero-index the level of the tree, the number of nodes on the xth level is equal to 2^x
