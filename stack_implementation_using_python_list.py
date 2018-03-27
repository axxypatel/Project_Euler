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


def test_stack_class():
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


def check_balanced_parentheses(parentheses_string):
    test_object = Stack()
    string_len = len(parentheses_string)
    status = True
    for temp in range(0, string_len):
        temp_char = parentheses_string[temp]
        if temp_char == "(":
            test_object.push(temp_char)
        else:
            if test_object.isempty():
                status = False
            else:
                test_object.pop()
    if test_object.isempty() and status:
        return True
    else:
        return False


print(check_balanced_parentheses('((()))'))
print(check_balanced_parentheses('(()))'))
