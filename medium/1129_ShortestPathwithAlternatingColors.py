"""
1129. Shortest Path with Alternating Colors
Medium
https://leetcode.com/problems/shortest-path-with-alternating-colors/
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        children = [[] for _ in range(n)] # 0 = red, 1 = blue
        edgeNum = 0
        for edge in redEdges:
            children[edge[0]].append([edge[1], 0, edgeNum]) # childInd, color, edgeNum
            edgeNum += 1
        for edge in blueEdges:
            children[edge[0]].append([edge[1], 1, edgeNum])
            edgeNum += 1
        res = [-1 for _ in range(n)]
        q = []
        q.append([0, -1, 0, set()]) #nodeInd, prev color, total length, used edges
        res[0] = 0
        while(len(q) > 0):
            node = q.pop(0)
            nodeInd = node[0]
            nodeColor = node[1]
            nodePath = node[2]
            nodeEdges = node[3]
            for child in children[nodeInd]:
                childInd = child[0]
                childColor = child[1]
                childEdge = child[2]
                if childColor == nodeColor:
                    continue
                if childEdge in nodeEdges:
                    continue
                childPath = nodePath + 1
                nodeEdges.add(childEdge)
                q.append([childInd, childColor, childPath, nodeEdges])
                res[childInd] = childPath if res[childInd] == -1 else min(res[childInd], childPath)
        
        return res
