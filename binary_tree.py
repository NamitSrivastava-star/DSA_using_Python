class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)
       
    def __repr__(self):
        return f'{self.root.left_child}|{self.root.value}|{self.root.right_child}'    

if __name__ == '__main__':
    root = BinaryTree(5)
    print(root)
