"""
695. Max Area of Island
Medium
https://leetcode.com/problems/max-area-of-island

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def getNeighborPixels(r, c, queue) -> int:
            count = 0
            if r > 0 and grid[r - 1][c] == 1:
                grid[r - 1][c] = 0
                count += 1
                queue.append([r - 1, c])
            if r < len(grid) - 1 and grid[r + 1][c] == 1:
                grid[r + 1][c] = 0
                count += 1
                queue.append([r + 1, c])
            if c > 0 and grid[r][c - 1] == 1:
                grid[r][c - 1] = 0
                count += 1
                queue.append([r, c - 1])
            if c < len(grid[r]) - 1 and grid[r][c + 1] == 1:
                grid[r][c + 1] = 0
                count += 1
                queue.append([r, c + 1])
            return count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                grid[row][col] = 0
                count = 1
                queue = []
                count += getNeighborPixels(row, col, queue)
                while len(queue) > 0:
                    pixel = queue.pop(0)
                    count += getNeighborPixels(pixel[0], pixel[1], queue)
                maxArea = max(maxArea, count)
        return maxArea
