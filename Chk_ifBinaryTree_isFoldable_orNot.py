# class to create a node with key, left child and right child.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to find whether the tree is foldable
def isFoldable(root):
    # Queue to store visited nodes
    q = []

    # Initially add the left and right nodes of root
    if root is not None:
        q.append(root.left)
        q.append(root.right)

    while len(q) != 0:

        # Remove the front 2 nodes to
        # check for None condition
        p = q.pop(0)
        r = q.pop(0)

        # If both are None, continue and check
        # the further elements
        if p is None and r is None:
            continue

        # If one of them is not None, then return False
        if (p is None and r is not None) or (p is not None and r is None):
            return False

        # Insert in the same order:
        #	1. left of left subtree
        #	2. right of right subtree
        #	3. right of left subtree
        #   4. left of right subtree

        q.append(p.left)
        q.append(r.right)
        q.append(p.right)
        q.append(r.left)

    # Only if the tree is foldable
    return True


# Driver code
# Insert data into the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.left.right = Node(5)

# Function call
if isFoldable(root):
    print("tree is foldable")
else:
    print("tree is not foldable")
