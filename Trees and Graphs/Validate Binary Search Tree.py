# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):

            # Empty Tree is Valid
            if not node:
                return True

            # Current Node's value must be between low and high
            if node.val <= low or node.val >= high:
                return False

            # Check Left and Right Subtree
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))

        return validate(root)
