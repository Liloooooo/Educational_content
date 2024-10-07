class BinaryTree: 
    def __init__(self): 
        self.root = None
     
    #main
    def insert_last(self, node):
        """ Insert node at rightmost position of tree. 
        Args: 
            node (BinaryNode): Node to be inserted
        Returns: 
            None 
        
        """
        
        assert isinstance(node, BinaryNode)
        if self.is_empty(): 
            self.root = node
        else: #tree contains at least one element     
            prev_last_node = self.root.last_in_subtree() 
            node.parent = prev_last_node
            prev_last_node.right = node 
   
    #main      
    def delete_first(self): #specific case of delete 
        """ Delete first node from self and return it. """
        if self.is_empty(): 
            print('Empty tree, nothing to delete')
            return 
        node = self.root.first_in_subtree() #O(h)
        if node != self.root: #O(1)
            node.parent.left = node.right 
        else: #O(1)
            self.root = node.right
        if node.right is not None: 
            node.right.parent = node.parent #can be None  
        return node
            
        
        

    
        
    #CC
    def delete_node(self, order_id): 
        """Delete Node with corresponding order_id and return deleted Node. If no Node deleted, return None."""
        node = self.find_node(order_id)
        if node is not None: 
            if node == self.root:
                if node.number_children == 0: 
                    self.root = None 
                if node.number_children() == 1: 
                    if node.right: 
                        self.root = node.right 
                    if node.left: 
                        self.root = node.left
                if node.number_children() == 2: 
                    successor_id = node.right.first_in_subtree().order_id
                    node.delete()
                    new_root = self.find_node(successor_id)
                    self.root = new_root
                    return node
            else: 
                return node.delete()
        print(f'no Node found with order_id {order_id}')
        return 
        
    #main or CC     
    def find_node(self, order_id): 
        """
        Return Node with corresponding order_id. Return None if no Node found and print according message. Return None if tree im empty and print according message.
        
        Args: 
            order_id (int): order_id to be searched for
            
        Returns: 
           BinaryNode with specified order_id, or None 
            
        """
        
        assert isinstance(order_id, int)
        if self.is_empty(): 
            return 
        return self.root.find(order_id)
    


    def is_empty(self): 
        """Return True if self is empty and False otherwise. """
        return self.root is None 
        

class BinaryNode: 
    def __init__(self, order_id, **kwargs):
        assert isinstance(order_id, int)
        self.order_id = order_id
        self.order_info = kwargs
        self.parent = None 
        self.left = None 
        self.right = None 
    
    #main or CC 
    def find(self, order_id): 
        """
        Return Node with corresponding order_id. Return None if no Node found and print according message. 
        
        Args: 
            order_id (int): order_id to be searched for
            
        Returns: 
           BinaryNode with specified order_id, or None 
            
        """

        if self.order_id == order_id: 
            return self
        if self.order_id > order_id: #search left tree 
            if self.left is not None: 
                self = self.left
                return self.find(order_id)
        else: 
            #search right tree 
            if self.right is not None: 
                self = self.right 
                return self.find(order_id)
        print('No node found')
        return 
    
    #CC
    def number_children(self): 
        return (self.right is not None) + (self.left is not None) 
    #CC
    def is_right_child(self): 
        """Bool indicating whether node itself is a right child to its parent."""
        return self.parent.right == self
    
    def is_root(self): #--> not needed?
        return self.parent is None 
    
    #CC 
    def delete(self): 
        """
        Delete self. Presumes node is not None and node is either not root or is root and has two children.

        Returns: self 

        """
        
        if self.number_children() == 0: #no children 
            if self.is_right_child(): #is right child to parent 
                self.parent.right = None 
            else: 
                self.parent.left = None 
            return self
        
        elif self.number_children() == 1: #one child 
            if self.is_right_child(): 
                if self.right is not None: #has right child 
                    self.right.parent = self.parent #set parent pointer of child
                    self.parent.right = self.right #set child pointer of parent 
                else: #has left child
                    self.left.parent = self.parent
                    self.parent.right = self.left 
            else: #self is left child to its parent 
                if self.right is not None: #self has right child 
                    self.right.parent = self.parent 
                    self.parent.left = self.right 
                else: #self has left child 
                    self.left.parent = self.parent 
                    self.parent.left = self.left 
            return self
        else: #two children 
            swap_node = self.right.first_in_subtree()
            self.order_id, swap_node.order_id = swap_node.order_id, self.order_id
            self.order_info, swap_node.order_info = swap_node.order_info, self.order_info #bit tricky
            return swap_node.delete()
    
    #main 
    def first_in_subtree(self): 
        #find first in subtree 
        """Return node that comes first in inherent traversal order """
        if self.left is None: 
            return self 
        else: 
            self = self.left 
            return self.first_in_subtree()
    #main                
    def last_in_subtree(self): 
        """Return node that comes last in inherent traversal order """
        if self.right is None: 
            return self
        else: 
            self = self.right
            return self.last_in_subtree()
            
            
            