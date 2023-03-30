# Represent a node of binary tree
class Node:
    def __init__(self, data):
        # Assign data to the new node, set left and right children to None
        self.data = data
        self.left = None
        self.right = None


class SmallestNode:
    def __init__(self):
        # Represent the root of binary tree
        self.root = None

        # smallestElement() will find out the smallest node in the binary tree

    def smallestElement(self, temp):
        # Check whether tree is empty
        if self.root is None:
            print("Tree is empty")
            return 0

        else:
            # Variable minimum will store temp's data
            minimum = temp.data

            # It will find the smallest element in left subtree
            if temp.left is not None:
                leftMin = self.smallestElement(temp.left)
                # If value of minimum is greater than leftMin then store the value of leftMin into minimum
                minimum = min(minimum, leftMin)

                # It will find the smallest element in right subtree
            if temp.right is not None:
                rightMin = self.smallestElement(temp.right)
                # If value of minimum is greater than rightMin then store the value of rightMin into minimum
                minimum = min(minimum, rightMin)
            return minimum


bt = SmallestNode()
# Add nodes to the binary tree
bt.root = Node(4)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(1)
bt.root.right.left = Node(5)
bt.root.right.right = Node(6)

# Display the smallest node in the binary tree
print("Smallest element in the binary tree: " + str(bt.smallestElement(bt.root)))
