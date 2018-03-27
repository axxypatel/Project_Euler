# Implement the queue data structure using list collections in python language


class Queue:
    def __init__(self):
        self.item_list = []

    def isempty(self):
        return self.item_list == []

    def enqueue(self, item):
        self.item_list.insert(0, item)

    def dequeue(self):
        self.item_list.pop()

    def size(self):
        return len(self.item_list)


def test_stack_class():
    sample_object = Queue()
    sample_object.enqueue(4)
    sample_object.enqueue('dog')
    sample_object.enqueue(4.7777)
    print("Added the value:", sample_object.item_list)

    sample_object.dequeue()
    print("Remove the top value:", sample_object.item_list)

    print("Size the queue:", sample_object.size())

    if sample_object.isempty():
        print("queue is empty")
    else:
        print("queue is not empty")


test_stack_class()
