# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right


# Function to print all nodes of a given level from left to right
def printLevelLeftToRight(root, level):
    if root is None:
        return False

    if level == 1:
        print(root.key, end=' ')
        return True

    # process left child before the right child
    left = printLevelLeftToRight(root.left, level - 1)
    right = printLevelLeftToRight(root.right, level - 1)
    return left or right


# Function to print all nodes of a given level from right to left
def printLevelRightToLeft(root, level):
    if root is None:
        return False

    if level == 1:
        print(root.key, end=' ')
        return True

    # process right child before the left child
    right = printLevelRightToLeft(root.right, level - 1)
    left = printLevelRightToLeft(root.left, level - 1)
    return right or left


# Function to print level order traversal of a given binary tree
def spiralOrderTraversal(root):
    if root is None:
        return

    # start from level 1 — till the height of the tree
    level = 1

    # run till either function returns false
    process = True

    while process:
        process = printLevelLeftToRight(root, level)
        level = level + 1

        if process:
            process = printLevelRightToLeft(root, level)
            level = level + 1


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    spiralOrderTraversal(root)