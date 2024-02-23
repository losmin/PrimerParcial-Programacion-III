class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if prev and root.val <= prev.val:
            return False

        prev = root
        root = root.right

    return True

# Example 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = isBST(root)
print(result)  # Output should be True

# Example 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

result = isBST(root)
print(result)  # Output should be False