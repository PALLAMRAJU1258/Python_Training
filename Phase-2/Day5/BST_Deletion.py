class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)
    elif key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

def minValueNode(node):
    current = node
    while current.left is not None :
        current = current.left
    return current

def deleteNode(root,key):
    if root is None :
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key :
        root.right = deleteNode(root.rigth,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)

root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)
print("Inorder Traversal of the Given tree:")
inorder(root)
print("\nDelete 20")
deleteNode(root,20)
print("Inorder Traversal of the modified tree:")
inorder(root)
print("\nDelete 30")
deleteNode(root,30)
print("Inorder Traversal of the modified tree:")
inorder(root)










        
            
