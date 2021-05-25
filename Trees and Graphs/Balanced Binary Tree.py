# Write a function to determine if a binary tree is super balanced
# Super Balanced = if the difference between the depths of any to leaf nodes is no greater than one

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isBalanced(root):

    # Tree with No Nodes is Superbalanced
    if root is None:
        return True

    # Short Circuit if 2 or more are found
    depths = []

    # List treated as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((root, 0))

    while len(nodes):

        # Pop node and its depth from the top of our stack
        node, depth = nodes.pop()

        # Case: Leaf Found
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                # 2 Cases:
                # 1. more than 2 different leaf depths
                # 2. 2 leaf depths that are more than 1 apart
                if ((len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False
        else:
            # Not a leaf - keep stepping down
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
