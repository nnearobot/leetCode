"""
1162. As Far from Land as Possible
Medium
https://leetcode.com/problems/as-far-from-land-as-possible/

"""
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return -1
        
        MAX_DIST = 2 * n
        distMap = [[MAX_DIST for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distMap[i][j] = 0
                else:
                    top = distMap[i - 1][j] + 1 if i > 0 else MAX_DIST
                    left = distMap[i][j - 1] + 1 if j > 0 else MAX_DIST
                    distMap[i][j] = min(distMap[i][j], top, left)
        
        res = -1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                bottom = distMap[i + 1][j] + 1 if i < n - 1 else MAX_DIST
                right = distMap[i][j + 1] + 1 if j < n - 1 else MAX_DIST
                distMap[i][j] = min(distMap[i][j], bottom, right)
                res = max(res, distMap[i][j])

        return -1 if res <= 0 or res == MAX_DIST else res


'''
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        lands = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    lands.append([i, j])
        if len(lands) == 0 or len(lands) == n * n:
            return -1
        if len(lands) >= n * n - 2:
            return 1

        distMap = [[n * n for j in range(n)] for i in range(n)]
        def dp(i, j, visitedMap):
            nonlocal res
            if visitedMap[i][j] == True:
                return
            visitedMap[i][j] = True
            if grid[i][j] == 0 and distMap[i][j] > 1:
                minDist = n * n
                if i > 0:
                    minDist = 1 if grid[i - 1][j] == 1 else min(minDist, distMap[i - 1][j] + 1)
                if i < n - 1:
                    minDist = 1 if grid[i + 1][j] == 1 else min(minDist, distMap[i + 1][j] + 1)
                if j > 0:
                    minDist = 1 if grid[i][j - 1] == 1 else min(minDist, distMap[i][j - 1] + 1)
                if j < n - 1:
                    minDist = 1 if grid[i][j + 1] == 1 else min(minDist, distMap[i][j + 1] + 1)

                if minDist >= distMap[i][j]:
                    return
                
                distMap[i][j] = minDist
                
            if i > 0 and grid[i - 1][j] == 0:
                dp(i - 1, j, visitedMap)
            if i < n - 1 and grid[i + 1][j] == 0:
                dp(i + 1, j, visitedMap)
            if j > 0 and grid[i][j - 1] == 0:
                dp(i, j - 1, visitedMap)
            if j < n - 1 and grid[i][j + 1] == 0:
                dp(i, j + 1, visitedMap)

        for land in lands:
            visitedMap = [[False for j in range(n)] for i in range(n)]
            dp(land[0], land[1], visitedMap)
 
        print(distMap)

        res = 0
        for i in range(n):
            for j in range(n):
                if distMap[i][j] < n * n:
                    res = max(res, distMap[i][j])

        return res


'''

'''
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        lands = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    lands.append([i, j])
        if len(lands) == 0 or len(lands) == n * n:
            return -1
        if len(lands) >= n * n - 2:
            return 1

        distMap = [[n * n for j in range(n)] for i in range(n)]
        def dp(i, j, step, visitedMap):
            if visitedMap[i][j] == True:
                return
            visitedMap[i][j] = True
            if grid[i][j] == 0:
                if step >= distMap[i][j]:
                    return
                distMap[i][j] = step
                
            if i > 0 and grid[i - 1][j] == 0:
                dp(i - 1, j, step + 1, visitedMap)
            if i < n - 1 and grid[i + 1][j] == 0:
                dp(i + 1, j, step + 1, visitedMap)
            if j > 0 and grid[i][j - 1] == 0:
                dp(i, j - 1, step + 1, visitedMap)
            if j < n - 1 and grid[i][j + 1] == 0:
                dp(i, j + 1, step + 1, visitedMap)

        for land in lands:
            visitedMap = [[False for j in range(n)] for i in range(n)]
            dp(land[0], land[1], 0, visitedMap)
 
        print(distMap)

        res = 0
        for i in range(n):
            for j in range(n):
                if distMap[i][j] < n * n:
                    res = max(res, distMap[i][j])

        return res



'''