# 1469. Find All The Lonely Nodes
# medium
# https://leetcode.com/problems/find-all-the-lonely-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append((root, False))
        while len(q):
            node, is_lonely = q.popleft()
            if is_lonely:
                res.append(node.val)
            if node.left:
                q.append((node.left, False if node.right else True))
            if node.right:
                q.append((node.right, False if node.left else True))
        return res
