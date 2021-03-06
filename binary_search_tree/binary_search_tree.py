"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""










































    # INSTRUCTIONS

'''     Implement the methods:
        
            `insert`, `contains`, `get_max`, and `for_each`
    
        on the BSTNode class.   '''


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



    # Insert the given value into the tree
    def insert(self, value):
        # Checks if the value/data already exsists in the tree
        if value == self.value:
            return
        
        if value < self.value:
            # Check if left element has a value
            if self.left:
                # Recursivly call the insert method
                self.left.insert(value)
            else:
                # Adds value/data as a child node on the left
                self.left = BSTNode(value)
        else:
                        # Check if right element has a value
            if self.right:
                # Recursivly call the insert method
                self.right.insert(value)
            else:
                # Adds value/data as a child node on the right
                self.right = BSTNode(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # If there's nothing in the tree, it contains nothing, False
        if (self == None):  
            return False

        # If the number we're checking is the root node of the tree, it exsists, True
        if (self.value == target):  
            return True

        # If the function above returns true on the left child value,
        # check_left = self.contains(self.left, target)
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while(current.right):
            current = current.right
        return current.value



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass











































    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
