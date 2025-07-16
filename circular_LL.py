class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

def __init__(self):
    temp = self.head
    ret_str = '['
    while temp is not None:
        ret_str += str(temp.data) + ','
        temp = temp.next
        if temp == self.head:
            break
    
    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str    
Ring.__str__ = __init__


def _get_last_node(self):
    if self.head is None:
        return None
    #case 2 is handle in case 3 also!
    if self.head.next == self.head:
        return self.head
    
    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next

    return temp
Ring._get_last_node = _get_last_node


def insert(self, index, value):
    new_node = Node(value)
    last_node = self._get_last_node()

    if index == 0:
        new_node.next = self.head
        self.head = new_node

        if last_node is None:
            self.head.next = self.head
        else:
            last_node.next = new_node
        return
    #In case we are putting the value on index > 0 and the list is empty
    if self.head is None: #and index > 0:
        raise IndexError("Can't insert at index = " + str(index) + " because, list is empty!")
    #For index > 0
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = new_node    
    new_node.next = temp
Ring.insert = insert


r = Ring()
r.insert(0, 1)
r.insert(1, 2)  
r.insert(2, 3)
r.insert(3, 4)
r.insert(4, 5)
print(r)  # Output: [1, 2, 3, 4, 5]
r.insert(2, 100)  # Insert 100 at index 2
print(r)  # Output: [1, 2, 100, 3, 4, 5]
r.insert(12, 200)  # Insert 200 at index 12
print(r)  # Output: [200, 1, 2, 100, 3, 4, 5]

#To verify if the ring exist or not
print(r._get_last_node().next == r.head)  # Output: True


def remove(self, value):
    if self.head is None:
        raise ValueError("List is empty, can't remove value: " + str(value))
    
    temp = self.head
    last_node = self._get_last_node()
    if temp.data == value:
        if last_node == self.head:
            self.head = None
        else:
            self.head = temp.next
            last_node.next = self.head
        return
    
    prev = temp
    temp = temp.next

    while temp != self.head:
        if temp.data == value:
            break
        prev = temp
        temp = temp.next
    if temp == self.head:
        raise ValueError("Value not found in the list: " + str(value))
    prev.next = temp.next

Ring.remove = remove

r.remove(100)  # Remove the value 100
print(r)  # Output: [200, 1, 2, 3, 4, 5]


#def push

#def pop 

