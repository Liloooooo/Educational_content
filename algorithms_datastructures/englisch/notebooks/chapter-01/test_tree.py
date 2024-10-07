import pytest
from tree import DatabaseTree, DatabaseNode

@pytest.fixture
def sample_tree(good_demo_node_alfred, good_demo_node_emma,  good_demo_node_fred, good_demo_node_george, good_demo_node_hans, good_demo_node_paolo,  good_demo_node_rita, good_demo_node_vanessa, good_demo_node_zoe): 
    node_alfred = good_demo_node_alfred
    node_emma = good_demo_node_emma
    node_fred = good_demo_node_fred
    node_george = good_demo_node_george
    node_hans = good_demo_node_hans
    node_paolo = good_demo_node_paolo
    node_rita = good_demo_node_rita
    node_vanessa = good_demo_node_vanessa
    node_zoe = good_demo_node_zoe
    node_fred.right = node_george
    node_emma.right = node_fred
    node_emma.left = node_alfred
    node_hans.left = node_emma
    node_vanessa.left = node_rita
    node_vanessa.right = node_zoe
    node_paolo.right = node_vanessa
    node_paolo.left = node_hans
    tree = DatabaseTree()
    tree.root = node_paolo
    return tree
                      
@pytest.fixture
def good_demo_node_alfred(): 
    return DatabaseNode(name='alfred', buyer_status = 'frequent', saved_payment = ['invoice', 'paypal'])

@pytest.fixture
def good_demo_node_emma(): 
    return DatabaseNode(name='emma')

@pytest.fixture
def good_demo_node_fred(): 
    return DatabaseNode(name='fred')

@pytest.fixture
def good_demo_node_george(): 
    return DatabaseNode(name='george')

@pytest.fixture
def good_demo_node_hans(): 
    return DatabaseNode(name='hans')


@pytest.fixture
def good_demo_node_paolo(): 
    return DatabaseNode(name='paolo')

@pytest.fixture
def good_demo_node_rita(): 
    return DatabaseNode(name='rita')

@pytest.fixture
def good_demo_node_vanessa(): 
    return DatabaseNode(name='vanessa')

@pytest.fixture
def good_demo_node_zoe(): 
    return DatabaseNode(name='zoe')

def test_node_init(good_demo_node_alfred):
    assert good_demo_node_alfred.name == 'alfred'  
    assert good_demo_node_alfred.add_info == {'buyer_status':'frequent', 'saved_payment':['invoice', 'paypal']}
                      
def test_node_init_errors(): 
    with pytest.raises(AssertionError): 
        bad_node = DatabaseNode(123)
    with pytest.raises(TypeError): 
        bad_node = DatabaseNode('name', 'invoice')
        
def test_find(sample_tree, good_demo_node_alfred, good_demo_node_emma, good_demo_node_zoe, good_demo_node_paolo):
    assert sample_tree.find('alfred') == good_demo_node_alfred
    assert sample_tree.find('emma') == good_demo_node_emma
    assert sample_tree.find('zoe') == good_demo_node_zoe 
    assert sample_tree.find('paolo') == good_demo_node_paolo #root
    assert sample_tree.find('freddy') is None 
    with pytest.raises(AssertionError): 
        sample_tree.find(name = 123)

def test_insert(sample_tree): 
    tree = sample_tree
    node_rahel = DatabaseNode(name = 'rahel')
    tree.insert(node_rahel)
    assert tree.find('rita').left == node_rahel 
    node_pablo = DatabaseNode(name = 'pablo')
    tree.insert(node_pablo)
    assert tree.find('hans').right == node_pablo
    bad_node = 'olga'
    with pytest.raises(AssertionError): #assertion error for bad node 
        tree.insert(bad_node)
        
def test_insert_empty(): 
    tree = DatabaseTree()
    node_barb = DatabaseNode(name = 'barb') #insert node into empty tree
    tree.insert(node_barb) 
    assert tree.root == node_barb #check if is root
    
    

        

        
  