class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.right = None
        self.left = None

def delete_Node(root, key):
    if not root:
        return root
    if root.val > key:
        root.left = delete_Node(root.left, key)
    elif root.val < key:
        root.right= delete_Node(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
    temp_val = root.right
    mini_val = temp_val.val
    while temp_val.left:
        temp_val = temp_val.left
        mini_val = temp_val.val
    root.right = delete_Node(root.right, root.val)
    return root

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)

print("ORIGINAL NODE: ")
print(preOrder(root))
res = delete_Node(root, 4)
print("DESPUES DE ELIMINAR UN NODO ESPECIFICO: ")
print(preOrder(res))