#Solution
class DatabaseTree: 
    """A basic binary tree data structure. 

    Attributes: 
        root (DatabaseNode): the root node. Defaults to None.

    """
    
#Solution
    def __init__(self): 
        self.root = None
    
#Solution 
    def find(self, name): 
        """
        Return DatabaseNode with provided user name. Return None if no node is found or if tree is empty.

        Args: 
            name (str): user name to be searched for. 

        Returns: 
           DatabaseNode with specified user name, or None if nothing found. 

        """
        
        assert isinstance(name, str)
        return self._find_rec(self.root, name)
    
#Solution 
    def _find_rec(self, sub_root, name):
        #recursive helper function for find. Returns DatabaseNode object or None if nothing found. 
        if sub_root is None: #base case 1: nothing found
            return sub_root
        if sub_root.name == name: #base case 2: node found  
            return sub_root 
        if name < sub_root.name: #recursive step
            new_root = sub_root.left
        if name > sub_root.name: 
            new_root = sub_root.right
        return self._find_rec(new_root, name)

#Solution 
    def insert(self, node): 
        """
        Insert DatabaseNode object into self. The binary search tree property must be preserved. 
    
        Args: 
            node (DatabaseNode): node to be inserted. 

        Returns: None 

        """
        
        assert isinstance(node, DatabaseNode)
        if self.root is None: 
            self.root = node
        else: 
            self._insert_rec(self.root, node)
            
#Solution    
    def _insert_rec(self, sub_root, node):
        #helper function: recursively inserts node
        if node.name < sub_root.name: 
            pos = sub_root.left #path to left 
            if pos is None: #base case: path is empty
                sub_root.left = node
                return #stop process            
        else: 
            pos = sub_root.right #path to right 
            if pos is None: #base case: path is empty
                sub_root.right = node 
                return #stop process
        self._insert_rec(pos, node) #recursive call 

            
            
#Solution
class DatabaseNode: 
    """A Node in DatabaseTree. 
    
    Args: 
        name (str): unique user name. 
        *kwargs: additional information to be stored.

    Attributes: 
        left (DatabaseNode): left child. Defaults to None.
        right (DatabaseNode): right child. Defaults to None.
        name (int): unique user name
        add_info (dict): additional information to be stored.

    """
    
#Solution
    def __init__(self, name, **kwargs):
        assert isinstance(name, str)
        self.name = name
        self.add_info = kwargs
        self.left = None 
        self.right = None 
    

 