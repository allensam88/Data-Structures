from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.stack = Stack()
        self.queue = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        # if value == self.value:
        #     return ?
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # base condition, when you hit the last largest 'right' leaf, return the value
        if self.right is None:
            return self.value
        # else... keep recursing thru
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # drill down the left side as far as you can go
        if node.left:
            self.left.in_order_print(node.left)

        # then queue up the lowest value
        self.queue.enqueue(node.value)
        # print out the lowest value as you dequeue it
        print(self.queue.dequeue())

        # if right leaf, recurse back up and send down the left again, hitting new lowest value
        if node.right:
            self.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # create queue
        # add root to queue
        # while queue is not empty
        # node = pop head of queue
        # DO THE THING!!! (print)
        # add children of node to queue
        self.queue.enqueue(node)
        while self.queue.size > 0:
            current_node = self.queue.dequeue()
            print(current_node.value)
            if current_node.left:
                self.queue.enqueue(current_node.left)
            if current_node.right:
                self.queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack.push(node)
        while self.stack.size > 0:
            current_node = self.stack.pop()
            print(current_node.value)
            if current_node.left:
                self.stack.push(current_node.left)
            if current_node.right:
                self.stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # queue up the current node and print
        self.queue.enqueue(node.value)
        print(self.queue.dequeue())

        # drill down the left side
        if node.left:
            self.left.pre_order_dft(node.left)

        # then dril down the right side
        if node.right:
            self.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # first drill down the left side as far as you can go
        if node.left:
            self.left.post_order_dft(node.left)

        # if right leaf, drill down right side too
        if node.right:
            self.right.post_order_dft(node.right)

        print(node.value)
