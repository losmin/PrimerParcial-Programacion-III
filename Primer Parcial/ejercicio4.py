class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def delete_Node(root, key):
    # If root doesn't exist, just return it
    if not root:
        return root
    
    # Find the node in the left subtree if key value is less than root value
    if key < root.val:
        root.left = delete_Node(root.left, key)
    
    # Find the node in the right subtree if key value is greater than root value
    elif key > root.val:
        root.right = delete_Node(root.right, key)
    
    # Delete the node if root.value == key
    else:
        # If there is no right child, delete the node and new root would be root.left
        if not root.right:
            return root.left
        # If there is no left child, delete the node and new root would be root.right
        elif not root.left:
            return root.right 
def deleteNode(root, key):
    if not root:
        return root
    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        
        # Both left and right children exist
        temp_val = root.right
        mini_val = temp_val.val
        
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        
        # Replace the node's value with the minimum value in the right subtree
        root.val = mini_val
        
        # Delete the minimum node in the right subtree
        root.right = deleteNode(root.right, root.val)
    
    return root

def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)

print("Original node:")
preorder(root)
result = deleteNode(root, 4)
print("After deleting specified node:")
preorder(result)