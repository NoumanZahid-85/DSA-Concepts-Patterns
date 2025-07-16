#doubly linked list

#Create a Node class    
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None  # Added for doubly linked list

#Create a LinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Added for doubly linked list

#Create a method to print the Doublylinkedlist
def __str__(self):
    #print(hex(id(None))) #check the id of None
    return_string = '['
    temp = self.head
    while temp is not None:
        #print(hex(id(temp.prev)), hex(id(temp)), hex(id(temp.next)))
        return_string += str(temp.data) + ', '
        temp = temp.next
    
    return_string = return_string.rstrip(', ')
    return_string += ']'
    return return_string
DoublyLinkedList.__str__ = __str__  #Add the __str__ method to the DoublyLinkedList class

#Create a Push method to add a new node at the start or end of the Doublylinkedlist
def Push(self, value):
    new_node = Node(value)

    if self.head  is None:
        print("Exec :Case 1")
        self.head = new_node
        return
    
    print("Exec :Case 2")
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
    new_node.prev = last  # Set the previous pointer for the new node
    return
DoublyLinkedList.Push = Push    #Add the Push method to the LinkedList class

l = DoublyLinkedList()
l.Push(1)
l.Push(2)
l.Push(3)
l.Push(4)
print(l)  # Output: [1, 2, 3, 4]


#Create a Pop method to remove the last node from the  doublylinkedlist
def Pop(self):
    if self.head is None:
        raise Exception("List is empty, cannot pop")
    
    if self.head.next is None:
        value = self.head.data
        self.head = None
        return value
    
    temp = self.head
    while temp.next is not None:
        temp = temp.next
    value = temp.data
    temp.prev.next = None  # Set the next pointer of the previous node to None
    temp.prev = None  # Set the previous pointer of the last node to None
    return value
DoublyLinkedList.Pop = Pop  #Add the Pop method to the LinkedList class

p = l.Pop()  # Output: 4

print(l)  # Output: [1, 2, 3]
print("Poped value is: ", p)  # Output: 4


#Craete to insert a new node at a specific index in the doubly linked list
def insert(self, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        return
    
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        temp = temp.next
        counter += 1
    if temp is None:  # If index is greater than the length of the list
        raise Exception("Index out of bounds")  
    else:
        new_node.prev = temp.prev
        temp.prev.next = new_node  # Set the next pointer of the previous node
        new_node.next = temp
        temp.prev = new_node 
DoublyLinkedList.insert = insert  #Add the insert method to the LinkedList class
l.insert(0, 5)  # Insert 5 at index 2
print(l)  # Output: [1, 2, 5, 3]


#Create a method to remove a node from the doublylinkedlist
def remove(self, value):
    temp = self.head
    if temp is not None:
        if temp.data == value:
            print("Exec :Case 1")
            print("Remove value is: ", temp.data)
            if self.head.next is not None:
                self.head = temp.next
                self.head.prev = None
            else:
                self.head = None
            temp = None
            return      
              
    print("Exec :Case 2")    
    while temp is not None:
        if temp.data == value:
            break
        prv = temp
        temp = temp.next
    if temp is None:
        print("Value not found in the list")
        return
    print("Remove value is: ", temp.data)
    if temp.next is not None:
        temp.next.prev = prv
        prv.next = temp.next
    else:
        prv.next = temp.next  # Set the next pointer of the previous node to None
        temp.prev = None  # Set the previous pointer of the last node to None

DoublyLinkedList.remove = remove  #Add the remove method to the LinkedList class
l.remove(9)  # Remove 5 from the list
print(l)  # Output: [1, 2, 3]