"""
	You may modify or reproduce.
	01:19:00 am Wednesday
	12-12-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated)
"""

#! /usr/bin/python3 /usr/bin/python

    #----Node----
class Node(object):

    #----CONSTRUCTOR----
    def __init__( self , value ):
        self.value = value
        self.next  = None

    #----SET----
    def set_value( self, value ):
        self.value = value

    #----GET----
    def get_value( self ):
        return self.value

    #----OVERRIDING----
    def __str__( self ):
        return "{0}".format( self.value )

    #----LinkedList----
class Singly(object):

    #----Constructor----
    def __init__( self ):
        self.head = None
        self.tail = None
        self._before = None
        self._after  = None
        self._current = None
        self.length = 0

    #----Head----
    def insert_at_front( self, value ):
        node = Node( value )
        if self._is_list_exist() is False:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self._incre_len()

    #----Tail----
    def insert_at_back( self, value ):
        node = Node( value )
        if self._is_list_exist() is False:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._incre_len()

    #----Before-Given----
    def insert_before( self, look_value, put_value ):
        node = Node( put_value )
        if self.head.get_value() == look_value:
            self.insert_at_front( put_value )
            self._incre_len()
        elif self._look_in( look_value ):
            node.next = self._current
            self._before.next = node
            self._incre_len()
        else:
            self._error("Sorry, {0} is not found.".format( look_value ))
        self._null_aux()

    #----After-Given----     
    def insert_after( self, look_value, put_value ):
        node = Node( put_value )
        if self.tail.get_value() == look_value:
            self.insert_at_back( put_value)
            self._incre_len()
        if self._look_in( look_value ):
            node.next = self._after
            self._current.next = node
            self._incre_len()
        else:
            self._error("Sorry, {0} is not found.".format( look_value ))
        self._null_aux()

    #----Head----
    def remove_from_front( self ):
        value = None
        if self._is_list_exist():
            temp_node = self.head
            value = temp_node.get_value()
            self.head = self.head.next
            self._decre_len()
            del temp_node
        self._null_aux()
        return value

    #----Tail----
    def remove_from_back( self ):
        value = None
        if self._is_list_exist():
            if self._look_in(self.tail.get_value()):
                temp_node = self._current
                value = temp_node.get_value()
                del temp_node
                self.tail = self._before
                self.tail.next = None
                self._decre_len()
        self._null_aux()
        return value

                           
#    def remove_before( self ):
#    def remove_after( self ):

    #----Iterate----
    def traverse( self ):
        lis = list()
        walker = self.head
        while walker is not None:
            lis.append(walker.get_value())
            walker = walker.next
        return lis
        
    #----Length----
    def get_length( self ):
        return self.length

    #----Search----
    def _look_in( self, value ):
        is_found = False
        if self._is_list_exist():
            self._current = self.head
            self._before = None
            self._after = self._current.next
            while self._current is not None:
                if self._current.get_value() == value:
                    is_found = True
                    break
                self._before = self._current
                self._current = self._current.next
                self._after = self._current.next
        return is_found

    #----Error----    
    def _error( self, message ):
        print(message)

    #----Increment----
    def _incre_len( self ):
        if self._is_list_exist():
            self.length = self.length + 1

    #----Decrement----
    def _decre_len( self ):
        if self._is_list_exist():
            self.length = self.length - 1

    #----RESET----
    def _null_aux( self ):
        self._current = None
        self._after = None
        self._before = None

    #----List-Exist----
    def _is_list_exist( self ):
        if self.head is None:
           return False
        else:
            return True

    #----Interface---
    def at_top(self):
        raise NotImplementedError

    #----Overriding----
    def __str__(self):
        return "{}".format(self.traverse())

    #----Destructor----
    def __del__(self):
        while self._is_list_exist():
            self.remove_from_front()

    #----Stack----
class Stack(Singly):

    #----CONSTRUCTOR----
    def __init__(self):
        Singly.__init__(self)

    #----PUSH----  
    def push(self, value):
        self.insert_at_front(value)

    #----POP----
    def pop(self):
        value = self.remove_from_front()
        return value

    #----EMPTY----
    def is_empty(self):
        is_ = self._is_list_exist()
        return False if is_ else True

    #----PEAK----
    def at_top(self):
        return self.head.get_value()

    #----OVERRIDING----
    def __str__(self):
        return Singly.__str__(self)

    #----Queue----
class Queue(Singly):

    #----CONSTRUCTOR----
    def __init__(self):
        Singly.__init__(self)

    #----ENQUE----  
    def enque(self, value):
        self.insert_at_back(value)

    #----DEQUE----
    def deque(self):
        value = self.remove_from_front()
        return value

    #----EMPTY----
    def is_empty(self):
        is_ = self._is_list_exist()
        return False if is_ else True

    #----PEAK----
    def at_top(self):
        return self.head.get_value()

    #----OVERRIDING----
    def __str__(self):
        return Singly.__str__(self)

    #----Parser----
class Parser(object):

    #----Constructor----
    def __init__(self, stream=None):
        self.stack = Stack()
        self.queue = Queue()
        self.stream = stream
        self._copy_stream()

    #----SET----
    def set_stream(self, stream):
        self.stream = stream
        self._copy_stream()

    #----COPY----
    def _copy_stream(self):
        if self.stream is not None:
            for char in self.stream:
                self.queue.enque(char)
    #----GET----
    def get_stream(self):
        return self.stream

    #----PARSE----
    def parse(self, error=False):
        is_balanced = True
        while self.queue.is_empty() != True:
            char = self.queue.deque() #--> DEQUE 
            if self._is_open(char):
                self.stack.push(char) #--> PUSH ON STACK 
            elif self._is_close(char):
                if self.stack.is_empty():
                    if error is True: #--> ERROR HANDLER ACTIVE ?
                        print("SyntaxError: Opening Parentheses Missing.")
                    is_balanced = False
                    break
                else:
                    self.stack.pop() #--> POP FROM STACK
            else:
                continue #--> IF AlphaNumeric 
        if self.stack.is_empty() == False: #--> STACK EMPTY ?
            if error is True:
                print("SyntaxError: Closing Parentheses Missing. ")
            is_balanced = False
        return is_balanced

    #----OPEN----
    def _is_open(self, char):
        return True if char in "(" else False

    #----CLOSE----
    def _is_close(self, char):
        return True if char in ')' else False
