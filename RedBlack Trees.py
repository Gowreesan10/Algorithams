class Node:
    #create and initialize a Node
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.color = 'Black'
        self.p = None

class RedBlackTree:

    #create a tree and initialize it as null
    def __init__(self) -> None:
        self.NIL = Node(None)
        self.root = self.NIL


    def left_rotate(self, node):
        r_node = node.right         # set y
        node.right = r_node.left    # turn y's left subtree into x's right subtree

        if r_node.left != self.NIL: #if y left is not null
            r_node.left.p = node    # set the y's left node parent

        r_node.p = node.p            # link x's parent to y

        if node.p == self.NIL:  # if x's parent is null x is a root node
            self.root = r_node
        elif node == node.p.left:  # set the x'parent appropriate node
            node.p.left = r_node
        else:
            node.p.right = r_node

        r_node.left = node           # put x on y's left
        node.p = r_node


    def right_rotate(self, node):
        l_node = node.left        # set x
        node.left = l_node.right  # turn x's right subtree into y's left subtree

        if l_node.right != self.NIL: #if x right is not null
            l_node.right.p = node # set the x's right node parent

        l_node.p = node.p  # link y's parent to x

        if node.p == self.NIL: #if y's parent is null y is a root node
            self.root = l_node
        elif node == node.p.right:# set the y'parent appropriate node
            node.p.right = l_node
        else:
            node.p.left = l_node

        l_node.right = node  # put y on x's right
        node.p = l_node


    def search(self, node, key):
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node


    def node_exists(self, key):
        node = self.search(self.root, key)
        return 'True' if node != self.NIL else 'False'


    def insert(self, value):
        if self.node_exists(value) !=  'False':
            print('Value already exists')
            return

        new_node = Node(value) # create a node with value
        parent_holder = self.NIL    # initialize parent_holder as null.
        temp = self.root   # initialize temp as root

        while temp != self.NIL: # traverse and find the node
            parent_holder = temp
            if new_node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        new_node.p = parent_holder             # set parent_holder as the parent of new_node

        if parent_holder == self.NIL:          # if parent_holder is null it means new_node is the first node/ root node
            self.root = new_node
        elif new_node.key < parent_holder.key: # else set the appropriate position of new_node in parent_holder
            parent_holder.left = new_node
        else:
            parent_holder.right = new_node

        new_node.left = self.NIL     # set new_node's left right and colour-red
        new_node.right = self.NIL
        new_node.color = "red"
        self.insert_fixup(new_node)  # fixes the red-red nodes


    def insert_fixup(self, node):
        while node.p.color == "red":      # loop until node's parent is red
            if node.p == node.p.p.left:   # if node's parent is a left child
                uncle = node.p.p.right    # get parent's sibiling (uncle)
                if uncle.color == "red":  # if uncle is red
                    node.p.color = "black"
                    uncle.color = "black"
                    node.p.p.color = "red"
                    node = node.p.p
                elif node == node.p.right: # if uncle is not red and node is a right node
                    node = node.p          # set the node's parent as node
                    self.left_rotate(node) # left rotate the node
                else:
                    node.p.color = "black" # set node's parent's color
                    node.p.p.color = "red" # set node's grand parent color
                    self.right_rotate(node.p.p) # right rotate grand parent
            else:
                uncle = node.p.p.left
                if uncle.color == "red":
                    node.p.color = "black"
                    uncle.color = "black"
                    node.p.p.color = "red"
                    node = node.p.p
                elif node == node.p.left:
                    node = node.p
                    self.right_rotate(node)
                else:
                    node.p.color = "black"
                    node.p.p.color = "red"
                    self.left_rotate(node.p.p)
        self.root.color = "black"


    def transplant(self, node, other_node):
        if node.p == self.NIL:       # if node's parent is null. node is root.
            self.root = other_node   # so other node will be the root
        elif node == node.p.left:    # if node is a left child
            node.p.left = other_node  # set other child as node's parent's child
        else:
            node.p.right = other_node
        other_node.p = node.p        # also set node's parent as other node's parent


    def tree_minimum(self, x):
        while x.left != self.NIL:  # iterates until there is no left child
            x = x.left
        return x


    def tree_maximum(self, x):
        while x.right != self.NIL: # iterates until there is no right child
            x = x.right
        return x


    def delete(self, del_node):
        y = del_node
        y_original_color = y.color

        if del_node.left == self.NIL:          
            x = del_node.right
            self.transplant(del_node, del_node.right) 
        elif del_node.right == self.NIL:       
            x = del_node.left
            self.transplant(del_node, del_node.left)  
        else:
            y = self.tree_minimum(del_node.right)  
            y_original_color = y.color
            x = y.right
            if y.p == del_node: 
                x.p = y         
            else:
                self.transplant(y, y.right)
                y.right = del_node.right
                y.right.p = y
            self.transplant(del_node, y)
            y.left = del_node.left
            y.left.p = y
            y.color = del_node.color

        if y_original_color == "black":
            self.delete_fixup(x)


    def delete_fixup(self, node):
        while node != self.root and node.color == "black":
            if node == node.p.left:
                sib = node.p.right
                if sib.color == "red":
                    sib.color = "black"
                    node.p.color = "red"
                    self.left_rotate(node.p)
                    sib = node.p.right
                if sib.left.color == "black" and sib.right.color == "black":
                    sib.color = "red"
                    node = node.p
                elif sib.right.color == "black":
                    sib.left.color = "black"
                    sib.color = "red"
                    self.right_rotate(sib)
                    sib = node.p.right
                sib.color = node.p.color
                node.p.color = "black"
                sib.right.color = "black"
                self.left_rotate(node.p)
                node = self.root
            else:
                sib = node.p.left
                if sib.color == "red":
                    sib.color = "black"
                    node.p.color = "red"
                    self.right_rotate(node.p)
                    sib = node.p.left
                if sib.right.color == "black" and sib.left.color == "black":
                    sib.color = "red"
                    node = node.p
                elif sib.left.color == "black":
                    sib.right.color = "black"
                    sib.color = "red"
                    self.left_rotate(sib)
                    sib = node.p.left
                sib.color = node.p.color
                node.p.color = "black"
                sib.left.color = "black"
                self.right_rotate(node.p)
                node = self.root
        node.color = "black"


    def delete_value(self, key):
        z = self.search(self.root, key)  
        if z != self.NIL:
            self.delete(z)
        else:
            print('EMPTY TREE')            


    def max_value(self):
        if self.root == None:
            return 'EMPTY TREE'
        max_node = self.tree_maximum(self.root)
        if max_node != self.NIL:
            return max_node.key
        else:
            return 'EMPTY TREE'


    def min_value(self):
        if self.root == None:
            return 'EMPTY TREE'
        min_node = self.tree_minimum(self.root)
        if min_node != self.NIL:
            return min_node.key
        else:
            return 'EMPTY TREE'



    def print_tree(self, node, indent, last):
        if node != self.NIL:
            if node.p != self.NIL:
                print(indent, end="")
                if last:
                    if(node.p.left == self.NIL):
                        print("└──", end="")
                    else:
                        print("├──", end="")
                    indent += "│  "
                else:
                    print("└──", end="")
                    indent += "   "
            color = "R" if node.color == "red" else "B"
            print(color + str(node.key))
            self.print_tree(node.right, indent, True)
            self.print_tree(node.left, indent, False)


    def printTree(self):
        self.print_tree(self.root, "", True)





tree = RedBlackTree()

inputs = input().split(" ") 
for i in inputs:
    tree.insert(int(i))

tree.printTree()
print()
operations_count = int(input())

for _ in range(operations_count):
    operation = input().split(" ")
    command = operation[0]
    if command == "Delete":
        tree.delete_value(int(operation[1]))
        tree.printTree()
    elif command == "Insert":
        tree.insert(int(operation[1]))
        tree.printTree()
    elif command == "Search":
        print(tree.node_exists(int(operation[1])))
    elif command == "Max":
        print(tree.max_value())
    elif command == "Min":
        print(tree.min_value())
    else:
        print("Invalid Operation")
    print()