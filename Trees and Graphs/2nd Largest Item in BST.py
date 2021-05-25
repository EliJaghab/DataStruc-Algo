# Solution to the find the largest element
def findLargest(root):
    curr = root
    while curr:

        # Traverse until the right child does not have a child
        if not curr.right:
            return curr.value
        curr = curr.right


def findSecondLargest(root):
    if (root is None or (root.left is None or root.right is None)):
        raise ValueError("Tree must have at least 2 nodes")

    curr = root

    while curr:
        # Case:
        # 1. Current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if curr.left and not curr.right:
            return(findLargest(curr.left))

        # Case 2:
        # Current is parent of largest, and largest has no children
        # so current is 2nd largest
        if (curr.right and not curr.right.left and not curr.right.right):
            return curr.value
        curr = curr.right

# Space: O(h)
# Time: O(1)
