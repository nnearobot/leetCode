# 382. Linked List Random Node
# Medium
# https://leetcode.com/problems/linked-list-random-node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        res = 0
        node = self.head
        i = 1
        while node:
            val = random.random()
            if val < 1 / i:
                res = node.val
            node = node.next
            i += 1
        
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()