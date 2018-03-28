# Implement the singly linked list implementation using python


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:    # every element add in front of the list near to head pointer so first element which is added will be available at last position
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def isempty(self):
        return self.head is None

    def remove(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                prev.next = current.next
                current.next = None
                return
            else:
                prev = current
                current = current.next

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


mylist = SinglyLinkedList()
mylist.add(53)
mylist.add(89)
mylist.add(100)
mylist.add(52)
mylist.add(48)
mylist.add(12)
print("Size of linked list", mylist.size())
mylist.remove(89)
mylist.remove(52)
print("Size of linked list", mylist.size())
print(mylist.search(100))
mylist.traverse()
