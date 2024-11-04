class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)


    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def count_nodes(self):
        return self._count_recursive(self.root) 

    def _count_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)

    def level_order_traversal(self):
        from collections import deque
        results = []
        if not self.root:
            return results

        quque = deque([self.root])
        while quque:
            current =  quque.popleft()
            result.append(current.value)
            if current.left:
                quque.append(current.left)
            if current.right:
                quque.append(current.right)  
        return result

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height =self._height_recursive(node.right) 
        return 1 + max(left_height. right_height)

    def is_valid_bst(self):
        return self.is_valid_recursive(self.root, float('-inf'), float('inf')) 

    def _is_valid_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if node.value <= min_value or node.value >=max_value:  
            return False
        return (self._is_valid_recursive(node.left, min_value, node.value))
        self._is_valid_recursive(node.right, node.value, max_value) 

if __name__ =="__main__":
    bst = BinarySearchTree()
    for value in [5, 7, 2, 8, 1, 3, 6]:
        bst.insert(value)

    print("Maximum value:", bst.find_max()) 
    print("Total nodes:", bst.count_nodes())  
    print("Level-order:", bst.level_order_traversal())  
    print("Height of the tree:", bst.height())  
    print("Is valid BST?", bst.is_valid_bst()) 

    print("In-order:", bst.inorder_traversal())  
    print("Pre-order:", bst.preorder_traversal())  
    print("Post-order:", bst.postorder_traversal())  

    
    bst.delete(3)
    print("After deleting 3:", bst.inorder_traversal()) 

    #conclusion
    
    
    



                     
