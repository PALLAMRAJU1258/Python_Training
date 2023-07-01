class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


node1 = BinaryTreeNode(34)
node2 = BinaryTreeNode(10)
node3 = BinaryTreeNode(23)
node4 = BinaryTreeNode(45)
node5 = BinaryTreeNode(78)
node6 = BinaryTreeNode(3)
node7 = BinaryTreeNode(98)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

print("Root Node:",node1.data)
print("Left child of Root Node:",node1.leftChild.data)
print("Right child of Root Node:",node1.rightChild.data)
print("Left child of left child of Root Node:",node1.leftChild.leftChild.data)
