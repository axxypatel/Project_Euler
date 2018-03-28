# Implement the doubly linked list abstract data type using python language


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        prev_node = self.head
        temp = Node(data)
        temp.next = self.head
        temp.prev = None
        if self.head is None:
            self.head = temp
        else:
            prev_node.prev = temp
            self.head = temp

    def isempty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def remove(self, data):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data == data:
                next_node = current_node.next
                prev_node.next = current_node.next
                current_node.next = None
                next_node.prev = prev_node
                return
            else:
                prev_node = current_node
                current_node = current_node.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False


mylist = DoublyLinkedList()
mylist.add(45)
mylist.add(68)
mylist.add(78)
mylist.add(96)
print("Size of the list", mylist.size())
mylist.remove(68)
mylist.traverse()

print(mylist.search(68))
