# Linked List Implementation in Python
# A linked list is a linear data structure where each element is a separate object.
# Each element (node) of a list is comprising of two items - the data and a reference to the next node.
# The last node has a reference to None.
# Linked lists are dynamic in size and can grow or shrink as needed.
# Advantages of Linked List:
# 1. Dynamic Size: Linked lists can grow and shrink in size as needed, unlike arrays which have a fixed size.
#create a Node class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

#Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

#Create a method to print the linked list
def __str__(self):
    return_string = '['
    temp = self.head
    while temp is not None:
        return_string += str(temp.data) + ', '
        temp = temp.next
    
    return_string = return_string.rstrip(', ')
    return_string += ']'
    return return_string
LinkedList.__str__ = __str__  #Add the __str__ method to the LinkedList class

#Create a Push method to add a new node at the start or end of the linked list
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
    return
LinkedList.Push = Push    #Add the Push method to the LinkedList class

l = LinkedList()
l.Push(1)
l.Push(2)
l.Push(3)
l.Push(4)
print(l)  # Output: [1, 2, 3, 4]

#Create a Pop method to remove the last node from the linked list
#Pop method to remove the last node from the linked list
def Pop(self):
    if self.head is None:
        raise Exception("List is empty, cannot pop")
    
    if self.head.next is None:
        value = self.head.data
        self.head = None
        return value
    
    temp = self.head
    while temp.next is not None:
        prv = temp
        temp = temp.next
    value = temp.data
    prv.next = None
    return value
LinkedList.Pop = Pop  #Add the Pop method to the LinkedList class

p = l.Pop()  # Output: 4

print(l)  # Output: [1, 2, 3]
print("Poped value is: ", p)  # Output: 4


def insert(self, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prv = temp
        temp = temp.next
        counter += 1
    new_node.next = temp
    prv.next = new_node 
LinkedList.insert = insert  #Add the insert method to the LinkedList class
l.insert(2, 5)  # Insert 5 at index 2
print(l)  # Output: [1, 2, 5, 3]

#Create a method to remove a node from the linked list
def remove(self, value):
    temp = self.head
    if temp is not None:
        if temp.data == value:
            print("Exec :Case 1")
            print("Remove value is: ", temp.data)
            self.head = temp.next
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
    prv.next = temp.next
    temp = None

LinkedList.remove = remove  #Add the remove method to the LinkedList class
l.remove(5)  # Remove 5 from the list
print(l)  # Output: [1, 2, 3]        



#ToDo Tasks:
def length(self):
    temp = self.head
    if self.head is None:
        print("List is empty")
        return 0
    counte = 0
    while temp is not None:
        counte += 1
        temp = temp.next
    return counte
LinkedList.length = length  #Add the length method to the LinkedList class
print("Length of the list is: ", l.length())  # Output: 3           

#Create a method to get the value on the specific index in linked list
def getValue(self, index):
    temp = self.head
    if index < 0:
        print("Index out of range")
        return None
    
    elif temp is None:
        print("List is empty")
        return None
    
    counter = 0
    while temp is not None:
        if counter == index:
            return temp.data
        temp = temp.next
        counter += 1
    print("Index out of range")
    return None
LinkedList.getValue = getValue  #Add the getValue method to the LinkedList class
l.getValue(1)  # Output: 3
print("Value at index 2 is: ", l.getValue(2))  # Output: 3
