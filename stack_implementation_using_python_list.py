# Implement stack data structure using list collection of python language


class Stack:
    def __init__(self):
        self.item_list = []

    def push(self, item):
        self.item_list.append(item)

    def pop(self):
        self.item_list.pop()

    def isempty(self):
        return self.item_list == []

    def peek(self):
        return self.item_list[len(self.item_list)-1]

    def size(self):
        return len(self.item_list)


sample_object = Stack()

sample_object.push(4)
sample_object.push('dog')
sample_object.push(4.7777)
print("Added the value:", sample_object.item_list)

sample_object.pop()
print("Remove the top value:", sample_object.item_list)

print("Show the top value:", sample_object.peek())

print("Size the stack:", sample_object.size())

if sample_object.isempty():
    print("Stack is empty")
else:
    print("Stack is not empty")
