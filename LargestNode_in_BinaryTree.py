# Represent a node of binary tree
class Node:
    def __init__(self, data):
        # Assign data to the new node, set left and right children to None
        self.data = data
        self.left = None
        self.right = None


class LargestNode:
    def __init__(self):
        # Represent the root of binary tree
        self.root = None

        # largestElement() will find out the largest node in the binary tree

    def largestElement(self, temp):
        # Check whether tree is empty
        if self.root is None:
            print("Tree is empty")
            return 0

        else:
            # Variable maximum will store temp's data
            maximum = temp.data

            # It will find the largest element in left subtree
            if temp.left is not None:
                leftMax = self.largestElement(temp.left)
                # Compare variable maximum with leftMax and store greater value into maximum
                maximum = max(maximum, leftMax)

                # It will find the largest element in right subtree
            if temp.right is not None:
                rightMax = self.largestElement(temp.right)
                # Compare variable maximum with rightMax and store greater value into maximum
                maximum = max(maximum, rightMax)
            return maximum


bt = LargestNode()
# Add nodes to the binary tree
bt.root = Node(15)
bt.root.left = Node(20)
bt.root.right = Node(35)
bt.root.left.left = Node(74)
bt.root.right.left = Node(55)
bt.root.right.right = Node(6)

# Display the largest node in the binary tree
print("Largest element in the binary tree: " + str(bt.largestElement(bt.root)))