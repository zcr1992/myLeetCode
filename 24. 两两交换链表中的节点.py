# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node = first_node
            head = first_node.next
        return dummy.next
