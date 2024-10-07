class BinaryTree: 
    def __init__(self): 
        self.root = None
        self.first = None 
        self.last = None
        
    def insert_last(self, node):
        """ Insert node at rightmost position of tree. 
        Args: 
            node (BinaryNode): Node to be inserted
        Returns: 
            None 
        
        """
        
        assert isinstance(node, BinaryNode)
        if self.is_empty(): 
            self.root, self.first, self.last = node, node, node
        else: #tree contains at least one element     
            self.last.right = node 
            node.parent = self.last
            self.last = node 
            
        
    def delete_first(self): 
        """ Delete first node from self and return it. """
        if self.is_empty(): 
            print('Empty tree, nothing to delete')
            return 
        node = self.first
        if node == self.root: 
            if self.last == self.root: #one element only 
                print('Tree emptied')
                self.root, self.first, self.last = None, None, None  
            else: #root/node has right child  
                self.root, self.first = self.right, self.right
                self.right.parent = None 
        else: #first must have a parent, and node must be parents left child  
            node.parent.left = node.right #can be None 
            if node.right is None: 
                tree.first = node.parent 
            else:#if right tree exists
                node.right.parent = node.parent #, assign new parent
                #assign new first 
                tree.first = node.right.first_in_subtree() #not constant time!!!!! abort first and last pointers 
        return node  
                
                
        
        
    def delete_node(self, order_id): 
        """ 
        Delete Node with corresponding order_id and return deleted Node. If no Node deleted, return None and print message
        """
        node = self.find_node(order_id)
        if node is not None: 
            if node == self.first: 
                return self.delete_first() #to be implemented, takes care of updating first 
            elif node == self.last: 
                print('Node cannot be deleted, is last node. Might be implemented in the future')
                return
            elif node == self.root: 
                print('node is root and not first node. Currently not implemented')
                return 
            return node.delete()
        print(f'no Node found with order_id {order_id}')
        return 
        

    
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
    
    def delete_first(self): 
        pass 
    
    def insert_last(self, node): 
        assert isinstance(node, BinaryNode)
        #to do

    def is_empty(self): 
        """Return True if self is empty and False otherwise. """
        return self.root is None 
        

class BinaryNode: 
    def __init__(self, order_id, **kwargs):
        self.order_id = order_id
        self.order_info = kwargs
        self.parent = None 
        self.left = None 
        self.right = None 
        
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
    
    def number_children(self): 
        return (self.right is not None) + (self.left is not None) 
    
    def is_right_child(self): 
        """Bool indicating whether node itself is a right child to its parent."""
        return self.parent.right == self
    
    def delete(self):
        """ Delete node that is not root node in tree"""

        if self.number_children() == 0: #no children 
            if not self.is_root_node():             
                if self.is_right_child(): #is right child to parent 
                    self.parent.right = None 
                else: 
                    self.parent.left = None 
            #else need to disconnect from tree
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
              
    def first_in_subtree(self): 
        #find first in subtree 
        if self.left is None: 
            return self 
        else: 
            self = self.left 
            return self.first_in_subtree()
                    
            
            
            