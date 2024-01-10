# 2385. Amount of Time for Binary Tree to Be Infected
# medium
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_map = collections.defaultdict(list)
        q = []
        q.append(root)
        while len(q) > 0:
            node = q.pop()
            if node.left:
                adj_map[node.val].append(node.left.val)
                adj_map[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adj_map[node.val].append(node.right.val)
                adj_map[node.right.val].append(node.val)
                q.append(node.right)
        print(adj_map)
        q = []
        q.append((start, -1, -1))
        path_len = 0
        while len(q) > 0:
            node = q.pop()
            path_len = max(path_len, node[2] + 1)
            for adj in adj_map[node[0]]:
                if adj == node[1]:
                    continue
                q.append((adj, node[0], node[2] + 1))
        return path_len
