from tkinter.tix import Tree


class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.right = None
        self.left = None
        
def array_to_bst(array):
    if not array:
        return None
    mid_num = len(array)//2
    node = TreeNode(array[mid_num])
    node.left= array_to_bst(array[:mid_num])
    node.right= array_to_bst(array[mid_num+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)
    
array = [1,2,3,4,5,6,7]

print(f"Array Original: {array}")
res = array_to_bst(array)
print(f"Array balanceado: {preOrder(res)}")