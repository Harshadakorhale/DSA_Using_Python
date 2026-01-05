class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root

    
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Before deletion:")
inorder(root)

root = deleteNode(root, 50)

print("\nAfter deletion:")
inorder(root)
