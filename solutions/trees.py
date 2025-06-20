"""
Tree Traversal Practice Exercise

Your task is to implement a binary tree and three traversal algorithms:
1. In-order traversal   (left -> root -> right)
2. Pre-order traversal  (root -> left -> right)
3. Post-order traversal (left -> right -> root)

First, implement the TreeNode class below.
Then, implement the three traversal methods in the BinaryTree class.
Finally, run the tests to verify your implementation.
"""


# TODO: Implement the TreeNode class
# The TreeNode class should have:
# - A value property to store the node's value
# - A left property to store the left child (default None)
# - A right property to store the right child (default None)


# TODO: Implement the BinaryTree class with traversal methods
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def inorder_traversal(self):
        """
        Perform an in-order traversal of the binary tree.
        Should return a list of values in the order they were visited.
        """
        result = []
        # TODO: Implement in-order traversal
        return result

    def preorder_traversal(self):
        """
        Perform a pre-order traversal of the binary tree.
        Should return a list of values in the order they were visited.
        """
        result = []
        # TODO: Implement pre-order traversal
        return result

    def postorder_traversal(self):
        """
        Perform a post-order traversal of the binary tree.
        Should return a list of values in the order they were visited.
        """
        result = []
        # TODO: Implement post-order traversal
        return result


# Test cases
def run_tests():
    # Test 1: Create and test an empty tree
    print("\nTest 1: Empty Tree")
    empty_tree = BinaryTree()
    assert empty_tree.inorder_traversal() == [], "Empty tree should return empty list"
    assert empty_tree.preorder_traversal() == [], "Empty tree should return empty list"
    assert empty_tree.postorder_traversal() == [], "Empty tree should return empty list"
    print("✓ Empty tree tests passed")

    # Test 2: Create and test a simple tree
    #       1
    #      / \
    #     2   3
    print("\nTest 2: Simple Tree")
    # TODO: Construct the simple tree using your TreeNode class
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # tree = BinaryTree(root)

    # Uncomment and run these tests after implementing your solution
    # assert tree.inorder_traversal() == [2, 1, 3], "Simple tree in-order traversal failed"
    # assert tree.preorder_traversal() == [1, 2, 3], "Simple tree pre-order traversal failed"
    # assert tree.postorder_traversal() == [2, 3, 1], "Simple tree post-order traversal failed"
    # print("✓ Simple tree tests passed")

    # Test 3: Create and test a complex tree
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #      /     \
    #     7       8
    print("\nTest 3: Complex Tree")
    # TODO: Construct the complex tree using your TreeNode class
    # root = TreeNode(1)
    # ... Add the remaining nodes ...
    # tree = BinaryTree(root)

    # Uncomment and run these tests after implementing your solution
    # assert tree.inorder_traversal() == [4, 2, 7, 5, 1, 3, 6, 8], "Complex tree in-order traversal failed"
    # assert tree.preorder_traversal() == [1, 2, 4, 5, 7, 3, 6, 8], "Complex tree pre-order traversal failed"
    # assert tree.postorder_traversal() == [4, 7, 5, 2, 8, 6, 3, 1], "Complex tree post-order traversal failed"
    # print("✓ Complex tree tests passed")


if __name__ == "__main__":
    run_tests()