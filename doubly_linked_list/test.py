# Team Members
#Sam, Mashima, Tony, Bryan
# Problem Description
    #How do you reverse a singly linked list without recursion? You may not store the list, or it's values, in another data structure.


# Understand
# What is the problem asking you to do?
    #reverse the order of an ssl in one pass

# What format do you need to deliver the solution in?
    #iterative single pass

# Plan
# How will you solve this problem?
    #reverse pointers iteratively by looking at 2 at a time and saving the pointer
# What is your pseudocode?
# def test(head):
#     first = head
#     second = head.next
#     first.next = None
#     while second != None:
#         pointer = second.next
#         second.next = first
#         first = second
#         second = pointer

# Execute
# Paste your code here:
# ???
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
four = Node(4)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)
head_node = Node(0, one)

# hi :)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
    # def add(self, value):
    #     self.next = Node(value)

# range Node?

def test(head):
    if head.next == None:
        return
    first = head
    second = head.next
    first.next = None
    while second != None:
        pointer = second.next
        second.next = first
        first = second
        second = pointer

arr1 = []
test(head_node)
def checker(node):
    var = node
    while var != None:
        print(var.value)
        var = var.next

checker(four)

# Reflect
# What is the time complexity of your solution?  How did you derive this?
'''

O(1) Space
O(n) Time
'''

# What elements of your solution can be improved?
#does not account for an node list of length 1 - fixed


