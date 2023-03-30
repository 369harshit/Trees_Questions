# A class to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to check if a given binary tree holds children-sum property
def hasChildrenSumProperty(root):
    # base case: empty tree
    if root is None:
        return 0

    # base case: leaf node
    if root.left is None and root.right is None:
        return root.data

    left = hasChildrenSumProperty(root.left)
    right = hasChildrenSumProperty(root.right)

    # if the root's value is equal to the sum of values at its left and right subtree
    if left != -float("inf") and right != -float("inf") and root.data == left + right:
        return root.data

    return -float("inf")


if __name__ == '__main__':

    root = Node(25)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if hasChildrenSumProperty(root) != -float('inf'):
        print('Binary tree holds children-sum property')
    else:
        print('Binary tree does not hold children-sum property')
