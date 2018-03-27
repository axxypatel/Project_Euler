# Implement the deque data structure using list collections of python language


class Deque:
    def __init__(self):
        self.item_list = []

    def isempty(self):
        return self.item_list == []

    def addfront(self, item):
        self.item_list.append(item)

    def addrear(self, item):
        self.item_list.insert(0, item)

    def removefront(self):
        return self.item_list.pop()

    def removerear(self):
        return self.item_list.pop(0)

    def size(self):
        return len(self.item_list)


def test_deque_class():
    sample_object = Deque()
    sample_object.addfront(4)
    sample_object.addrear('dog')
    sample_object.addfront(4.7777)
    print("Added the value:", sample_object.item_list)

    sample_object.removefront()
    print("Remove the front value:", sample_object.item_list)

    sample_object.removerear()
    print("Remove the rear value:", sample_object.item_list)

    print("Size the queue:", sample_object.size())

    if sample_object.isempty():
        print("queue is empty")
    else:
        print("queue is not empty")


test_deque_class()
