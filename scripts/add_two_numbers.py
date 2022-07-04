# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        inputs = [l1, l2]
        input_sum = 0
        output = []
        for linked_list in inputs:
            node = linked_list
            number = ''
            while node:
                number = number + str(node.val)
                node = node.next
            input_sum = input_sum + int(number[::-1])

        reversed_digit = str(input_sum)[::-1]
        for index in range(len(reversed_digit)):
            output.append(ListNode(reversed_digit[index]))

        for index in range(len(output) - 1):
            output[index].next = output[index + 1]

        if output:
            return output[0]
        else:
            return ListNode()
