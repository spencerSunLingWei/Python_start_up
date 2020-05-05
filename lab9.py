''' In this lab, you are to create a sorting algorithm to sort a linked list
    using recursion.

    class Node is provided. Queue class functions 'append' and 'find_max_value_position'
    are provided. Use them to help you complete the rest of the functions.

    You need to first complete the three individual functions:
        concatenate
        max_value
        remove_max
    This should not take a long time to complete.

    The main part of this lab is to complete selectionSort. You need to think of
    how you should call the functions in selectionSort so that the algorithm
    can sort and return the sorted linked list using recursion.

    Each of the individual functions will be tested in the test cases
    as well as the selectionSort function.
'''

class Node:
    ''' Each node in the link list '''
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

class Queue:
    ''' Linked List class '''
    def __init__(self, l =[]):
        self.length = 0
        self.head = None
        self.tail = None

        if len(l)!=0:
            for ll in l:
                self.append(ll)

    def __str__(self):
        ''' (Queue) -> str
        Returns a string representation of the queue
        >>> Queue(['a', 'bc']).__str__()
        "['a', 'bc']"
        >>> print(Queue(['a', 'bc']))
        ['a', 'bc']
        '''
        node = self.head
        l = []
        while node != None:
            l.append(node.cargo)
            node = node.next

        return(str(l))

    def append(self, cargo):
            '''(Queue, type_of_cargo) -> NoneType
            Adds an element at the tail of the linked list, as the last element.
             >>> 
             [1, 2]
            '''
            node = Node(cargo)

            if self.length == 0:

                self.head = node
                self.tail = node
                self.length += 1

            else:
                self.tail.next = node
                self.tail = node
                self.length += 1


    def find_max_value_position(self):
        '''(Queue) -> int
        Returns the position in the queue of the maximal cargo value. If the
        maximal value   appears several times, the position closest to the head
        of the Queue is returned.

        >>> Queue([1]).find_max_value_position()
        0
        >>> Queue([1,0]).find_max_value_position()
        0
        >>> Queue([0,1]).find_max_value_position()
        1
        >>> Queue([2,0,1,0,4]).find_max_value_position()
        4
        >>> q = Queue([64, 25, 12, 22])
        q.find_max_value_position()
        0
        '''
        position = 0
        max_index = 0

        if self.length == 0:
            return -1
        else:
            max_value = self.head.cargo
            node = self.head.next

            while node!= None:
                if node.cargo > max_value:
                    max_value = node.cargo
                    max_index = position +1
                node = node.next
                position += 1
                #print(max_value, max_index)
            return max_index

    def concatenate(self, other):
        '''(Queue, Queue) -> NoneType
        Appends the second queue at the end of the first input queue.

        >>> q1 = Queue([1,0,0])
        >>> q2 = Queue([2])
        >>> q1.concatenate(q2)
        >>> print(q1)
        [1, 0, 0, 2]
        >>> q1 = Queue([1,0,0])
        >>> q2 = Queue([])
        >>> q1.concatenate(q2)
        >>> print(q1)
        [1, 0, 0]
        >>> q1 = Queue([])
        >>> q2 = Queue([1])
        >>> q1.concatenate(q2)
        >>> print(q1)
        [1]
        '''
        

        if self.length == 0:

            self.head = other.head
            self.tail = other.tail
            self.length += other.length

        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length


        

    def max_value(self):
        '''(Queue) -> type-of-cargo
        Returns the maximal cargo value in the queue. If the list is empty,
        the function returns None. The max value is not removed from the queue.

        >>> q = Queue()
        >>> print(q.max_value())
        None
        >>> q = Queue([1])
        >>> q.max_value()
        1
        >>> q = Queue([1,0,0])
        >>> q.max_value()
        1
        '''

        position = 0
        max_index = 0

        if self.length == 0:
            print('None')
        else:
            max_value = self.head.cargo
            node = self.head.next

            while node!= None:
                if node.cargo > max_value:
                    max_value = node.cargo
                    max_index = position +1
                node = node.next
                position += 1
                #print(max_value, max_index)
            return max_value


    def remove_max(self):
        '''(Queue) -> NoneType
        Removes the first occurence of the maximal cargo value from the input
        Queue. If the input Queue is empty, nothing is removed. If the Queue
        has one element, that element is removed and the queue becomes empty.
        The legth of the input Queue is also decreased by 1.

        >>> q = Queue([1,0])
        >>> q.remove_max()
        >>> print(q)
        [0]
        >>> q = Queue([1,0,2,0])
        >>> q.remove_max()
        >>> print(q)
        [1, 0, 0]
        >>> q = Queue([1])
        >>> q.remove_max()
        >>> print(q)
        []
        >>> q = Queue()
        >>> q.remove_max()
        >>> print(q)
        []
        >>> q = Queue([0,3])
        >>> q.remove_max()
        >>> print(q)
        [0]
        '''

        if self.length == 0:
            result= []
        else:
            item = self.max_value()

            previous = None
            current = self.head

            while current != None and current.cargo != item:
                previous = current
                current = current.next
            if current != None:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                current.next = None
                self.length -= 1
            else:
                self = Queue([])
        


def selectionSort(unsorted_linked_list):
    '''(Queue) -> Queue
    Returns a copy of the input Queue sorted in descending order
    >>> print(selectionSort(Queue([5,2,1,3])))
    [1, 2, 3, 5]
    >>> print(selectionSort(Queue([])))
    []
    >>> print(selectionSort(Queue([1])))
    [1]
    >>> print(selectionSort(Queue([2,1])))
    [1, 2]
    >>> print(selectionSort(Queue([64, 25, 12, 22, 11])))
    [11, 12, 22, 25, 64]
    '''
    
    
##    def function(unsorted_linked_list):
##        sorted_linked_list=Queue([])
##        maximum_value = unsorted_linked_list.max_value()
##        sorted_linked_list.append(maximum_value)
##        unsorted_linked_list.remove_max()
##        return sorted_linked_list,unsorted_linked_list
##
##
##
##    while unsoterd_linked_list.length>0:
##        function(unsorted_linked_list)
    
        
    
    
    
        
    if unsorted_linked_list.length<=1:
        return unsorted_linked_list
    else:
        
        
        sorted_linked_list=Queue([])
        maximum_value = unsorted_linked_list.max_value()
        sorted_linked_list.append(maximum_value)
        unsorted_linked_list.remove_max()
            
        sorted_linked_list.concatenate(selectionSort(unsorted_linked_list))
        return sorted_linked_list
    
    
        
        
        

        
        
        





















    
