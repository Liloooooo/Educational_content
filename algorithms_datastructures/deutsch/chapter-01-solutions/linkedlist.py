#Lösung
class LLQueue:
    """
    A queue implemented as a linked list.

    Attributes:
        head (LinkedNode): Head node of Linked list. Defaults to None. 
        tail (LinkedNode): Tail node of linked list. Defaults to None. 
        
    """
    
#Lösung 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.length = 0

#Lösung
    def __len__(self): 
        """Return number of LinkedNode objects in self."""
        return self.length

#Lösung
    def insert_last(self, data): 
        """
        Insert a new node at the last position of the queue. 
        
        Args: 
            data (LinkedNode): the node to be appended. 
        
        Returns: 
            None 
            
        """
        
        assert isinstance(data, LinkedNode)
        self.length += 1 
        if self.tail is None: 
            self.tail, self.head = data, data
        else: 
            self.tail.next = data
            self.tail = data 

#Lösung
    def delete_first(self): 
        """
        Delete first node. Print message if queue contains no elements, and nothing is deleted. 
        
        Returns: 
            Deleted node (LinkedNode), None is self was empty.  
            
        """
        
        if self.tail is None: 
            print('Queue contains no elements')
            return None
        self.length -= 1
        pop = self.head
        self.head = self.head.next 
        if self.head is None: 
            self.tail = None 
        return pop
    
#Lösung
    def find_previous(self, order_id, start_node): 
        #helper function to recursively search for previous node
        if start_node.order_id == order_id: 
            print('Node itself has order_id')
            return None 
        if start_node.next is None: 
            print(f'No node with order_id {order_id} found')
            return None 
        if start_node.next.order_id == order_id: 
            return start_node 
        else: 
            return self.find_previous(order_id, start_node.next)
    
#Lösung
    def delete_node(self, order_id): 
        """
        Delete node with specific order_id. Return deleted node, and none if nothing found. Print message if nothing is found. 
        
        Args: 
            order_id (int): unique order id of LinkedNode object to be deleted from self. 
            
        Returns: 
            Deleted node (LinkedNode), None is self was empty.  
            
        """

        assert isinstance(order_id, int)
        if self.tail is None: #empty queue
            return None
        node_prev = self.find_previous(order_id, self.head)
        if node_prev is None: #node does not exist
            if self.head.order_id == order_id: 
                return self.delete_first()
            return None 
        node = node_prev.next  
        node_prev.next = node.next
        self.length -= 1 
        if self.tail == node: 
            self.tail = node_prev
        return node 
        
        
    
    
class LinkedNode: 
    """
    A node in a linked list.
    
    Args: 
        order_id (int): a unique id that is assigned to a specific order 
        **kwargs: additional data to be stored for an order.

    Attributes:
        order_id (int): a unique id that is assigned to a specific order 
        order_info (dict): additional data to be stored for an order. Defaults to {}.
        next (LinkedNode): next node, defaults to None. 
    """
    
#Lösung
    def __init__(self, order_id, **kwargs): 
        assert isinstance(order_id, int), 'order_id must be an integer'
        self.order_id = order_id
        self.order_info = kwargs
        self.next = None
  