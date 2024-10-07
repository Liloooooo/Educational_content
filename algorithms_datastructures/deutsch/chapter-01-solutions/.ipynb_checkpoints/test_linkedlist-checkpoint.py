import pytest
from linkedlist import LinkedNode, LLQueue

NoneType = type(None)


@pytest.fixture
def good_demo_node_1(): 
    return LinkedNode(order_id=14, product_id=[123], payment='invoice', message= 'call beforehand')
                      
@pytest.fixture
def good_demo_node_2(): 
    return LinkedNode(order_id=24)

@pytest.fixture
def good_demo_node_3(): 
    return LinkedNode(order_id=34)

@pytest.fixture
def good_demo_node_4(): 
    return LinkedNode(order_id=44)
 
@pytest.fixture
def full_queue(good_demo_node_1, good_demo_node_2): 
    llqueue = LLQueue()
    llqueue.insert_last(good_demo_node_1)
    llqueue.insert_last(good_demo_node_2)
    return llqueue

@pytest.fixture
def very_full_queue(good_demo_node_1, good_demo_node_2, good_demo_node_3, good_demo_node_4): 
    llqueue = LLQueue()
    llqueue.insert_last(good_demo_node_1)
    llqueue.insert_last(good_demo_node_2)
    llqueue.insert_last(good_demo_node_3)
    llqueue.insert_last(good_demo_node_4)
    return llqueue

  
def test_node_init(good_demo_node_1, good_demo_node_2):
    assert good_demo_node_1.order_id == 14  
    assert good_demo_node_1.order_info == {'product_id':[123], 'payment':'invoice', 'message':'call beforehand'}
    assert good_demo_node_2.order_id == 24
    assert good_demo_node_2.order_info == {} 
                      
def test_node_init_errors(): 
    with pytest.raises(AssertionError): 
        bad_node = LinkedNode('123') #assertion error if order_id is string 
    with pytest.raises(TypeError): 
        bad_node = LinkedNode(14, 'invoice') #typeerror if keyword not specified for **kwargs


def test_insert_last(good_demo_node_1, good_demo_node_2):
    queue = LLQueue()
    queue.insert_last(good_demo_node_1) #queue with one element
    assert queue.head == good_demo_node_1 
    assert queue.tail == good_demo_node_1
    assert good_demo_node_1.next is None #end of queue
    #new queue
    queue = LLQueue()
    queue.insert_last(good_demo_node_1)
    queue.insert_last(good_demo_node_2) #queue with two elements 
    assert queue.head == good_demo_node_1 #check if head correctly set
    assert queue.tail == good_demo_node_2 #check if tail is set
    assert good_demo_node_1.next == good_demo_node_2
    assert good_demo_node_2.next is None #end of queue
                      
def test_insert_last_errors(): 
    queue = LLQueue()
    with pytest.raises(AssertionError): 
        queue.insert_last(15) #insert_last takes LinkedNode object 

def test_delete_first(full_queue, good_demo_node_1, good_demo_node_2): 
    queue = full_queue #two element queue 
    pop1 = queue.delete_first() #one element left
    assert pop1 == good_demo_node_1
    assert queue.head == good_demo_node_2 #check new head
    assert queue.tail == good_demo_node_2 #check new tail 
    pop2 = queue.delete_first() #empty queue 
    assert pop2 == good_demo_node_2 
    assert queue.head is None #check new head 
    assert queue.tail is None #check new tail 
    pop3 = queue.delete_first() #was already empty, return None 
    assert pop3 is None 
    assert queue.head is None
    assert queue.tail is None
    
def test_delete_node(very_full_queue, good_demo_node_1, good_demo_node_2, good_demo_node_3, good_demo_node_4):
    queue = very_full_queue
    pop = queue.delete_node(order_id=24) #standard case
    assert pop == good_demo_node_2
    assert queue.head == good_demo_node_1
    assert queue.tail == good_demo_node_4
    assert good_demo_node_1.next == good_demo_node_3
    
    pop = queue.delete_node(order_id=10) #special case: nothing found 
    assert pop is None
    assert queue.head == good_demo_node_1
    assert queue.tail == good_demo_node_4
    assert good_demo_node_1.next == good_demo_node_3
    
    pop = queue.delete_node(order_id=14) #special_case: delete first 
    assert pop == good_demo_node_1
    assert queue.head == good_demo_node_3
    assert queue.tail == good_demo_node_4
    
    pop = queue.delete_node(order_id=44) #special_case: delete last 
    assert pop == good_demo_node_4
    assert queue.head == good_demo_node_3
    assert queue.tail == good_demo_node_3
    assert good_demo_node_3.next is None 
    
    pop = queue.delete_node(order_id=34) #special case: empties queue
    assert pop == good_demo_node_3
    assert queue.head is None 
    assert queue.tail is None 
    
    
def test_delete_node_2(very_full_queue, good_demo_node_1, good_demo_node_2, good_demo_node_3, good_demo_node_4): #alternative order
    queue = very_full_queue #four element queue
    pop = queue.delete_node(order_id=34) #delete third 
    assert pop == good_demo_node_3
    assert queue.head == good_demo_node_1
    assert queue.tail == good_demo_node_4
    assert good_demo_node_2.next == good_demo_node_4
    
    pop = queue.delete_node(order_id = 44) #delete last
    assert pop == good_demo_node_4
    assert queue.head == good_demo_node_1
    assert queue.tail == good_demo_node_2 #check tail 
    assert good_demo_node_2.next is None
    
 
def test_len(very_full_queue, good_demo_node_1, good_demo_node_2, good_demo_node_3, good_demo_node_4): 
    queue = very_full_queue #four element queue 
    assert len(queue) == 4 #first sanity checks for delete_node() and delete_first()
    queue.delete_first() 
    assert len(queue) == 3
    queue.delete_node(order_id=14) #not existant anymore --> nothing deleted 
    assert len(queue) == 3
    queue.delete_node(order_id=34) 
    assert len(queue) == 2
    queue.delete_node(order_id=10) #not existant 
    assert len(queue) == 2
    queue.delete_first()
    assert len(queue) == 1
    queue.delete_first()
    assert len(queue) == 0
    queue.insert_last(good_demo_node_4) #sanity check insert_last()
    assert len(queue) == 1 
    queue.insert_last(good_demo_node_3)
    assert len(queue) == 2