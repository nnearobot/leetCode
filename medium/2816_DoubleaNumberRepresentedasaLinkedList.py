# 2816. Double a Number Represented as a Linked List
# medium
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def double_node(node: ListNode()):
            node.val *= 2
            if node.next:
                next_node = double_node(node.next)
                if next_node.val >= 10:
                    next_node.val %= 10
                    node.val += 1
            return node

        head = double_node(head)
        if head.val >= 10:
            new_node = ListNode()
            new_node.val = head.val % 10
            new_node.next = head.next
            head.val = 1
            head.next = new_node

        return head
