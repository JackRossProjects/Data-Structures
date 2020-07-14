"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList

class Queue:
# Queue - Add (Enqueue) to the back of the queue (tail),
#         remove (Dequeue) from front (head).

    def __init__(self):
        # Initialize this queue to the empty queue
        self.size = 0
        # Use the LinkedList class as storage
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        # Creates a node from the value,
        # Checks if list is empty,
        # Adds value as tail
        self.size += 1

    def dequeue(self):
        data = self.storage.remove_head()
        # Checks if list is empty,
        # Checks if head and tail are pointing at same node
        # If so, delete head and tail referance
        # Else set the new head to the node after the head
        if data != None:
            self.size -= 1
            return data
