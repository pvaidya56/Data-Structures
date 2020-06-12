"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create a new node
        new_node = ListNode(value, None, None)
        #check if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #check if DLL is empty
        if not self.head:
            return
        #check if DLL has only one element
        if not self.head.next:
            self.head = None
            self.tail = None
            self.length = self.length - 1

        removedNode = self.head
        self.head.next.prev = self.head.prev
        self.head = self.head.next
        self.length = self.length - 1
        return removedNode

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #create a new node
        new_node = ListNode(value, None, None)
        self.length += 1
        #check if DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #check if empty
        if not self.tail:
            return
        #if DLL only has one element
        if not self.tail.prev:
            removedNode = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return removedNode
        removedNode = self.tail
        self.tail.prev.next = self.tail.next
        self.tail = self.tail.prev
        self.length-=1
        return removedNode.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #check if only one element
        if self.head == node:
            return
        elif self.length > 1 and node.next != None:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.add_to_head(node.value)
            self.length -= 1

        elif self.length > 1 and node.next == None:
            node.prev.next = node.next
            self.tail = node.prev
            self.add_to_head(node.value)
            self.length -= 1
        return

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail == node:
            return
        elif self.length > 1 and node.prev != None: 
            node.prev.next = node.next
            node.next.prev = node.prev
            self.add_to_tail(node.value)
            self.length-=1

        elif self.length > 1 and node.prev == None:
            node.next = self.head
            node.next.prev = node.prev
            self.add_to_tail(node.value)
            self.length-=1

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head:
            return
        elif node == self.head:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = self.head.prev
                self.head = self.head.next
        elif node == self.tail:
            if self.length == 1:
                self.head = None
                self.tail = None
            else: self.tail.prev.next = self.tail.next
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next 
            node.next.prev = node.prev
        self.length -= 1
        return
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next

        while current != None:
            if current > max_value:
                max_value = current.value
            current = current.next

        return max_value
