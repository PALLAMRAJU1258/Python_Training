class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printInorder(root):
    if root :
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)

def printPreorder(root):
    if root :
        print(root.data,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root :
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data,end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("PRE-ORDER:")
printPreorder(root)
print()
print("IN-ORDER:")
printInorder(root)
print()
print("Post-ORDER:")
printPostorder(root)
print()
            
