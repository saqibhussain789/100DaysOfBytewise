class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Function to take input from user and perform BST operations
def user_input_bst():
    bst = BST()
    root = None
    
    # Taking input for the initial BST creation
    keys = list(map(int, input("Enter the elements to insert into the BST, separated by spaces: ").split()))
    for key in keys:
        root = bst.insert(root, key)
    
    # Display the inorder traversal of the BST
    print("Inorder traversal of the given tree:")
    bst.inorder(root)
    print()
    
    # Taking input for deletion
    delete_key = int(input("Enter the element to delete from the BST: "))
    root = bst.delete(root, delete_key)
    
    # Display the inorder traversal of the modified BST
    print("Inorder traversal of the modified tree:")
    bst.inorder(root)
    print()
    
    # Taking input for search
    search_key = int(input("Enter the element to search in the BST: "))
    result = bst.search(root, search_key)
    print(f"Node found: {result.val}" if result else "Node not found")

# Test the BST with user input
user_input_bst()
