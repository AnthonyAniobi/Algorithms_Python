class Node:
    current:str

    def __init__(self, current, left=None, right=None ) -> None:
        self.current = current
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.current)

class Tree:
    root:Node

    def in_order_trasversal(self, node:Node):
        if node:
            self.in_order_trasversal(node.left)
            print(node)
            self.in_order_trasversal(node.right)
    
    def pre_order_trasversal(self, node:Node):
        if node:
            print(node)
            self.pre_order_trasversal(node.left)
            self.pre_order_trasversal(node.right)
    
    def post_order_trasversal(self, node:Node):
        if node:
            self.post_order_trasversal(node.left)
            self.post_order_trasversal(node.right)
            print(node)
    

if __name__ == '__main__':
    node7 = Node(7)
    node6 = Node(6)
    node4 = Node(4)
    node3 = Node(3)
    node5 = Node(5, node6, node7)
    node2 = Node(2, node3, node4)
    node1 = Node(1, node2, node3)

    tree = Tree()
    tree.root = node1

    tree.pre_order_trasversal(node1)
