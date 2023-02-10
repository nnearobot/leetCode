# 733. Flood Fill
# Easy
# https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        queue = []
        oldColor = image[sr][sc]
        def getNeighborPixels(r, c):
            nonlocal color, oldColor
            if r > 0 and image[r - 1][c] == oldColor:
                image[r - 1][c] = color
                queue.append([r - 1, c])
            if r < len(image) - 1 and image[r + 1][c] == oldColor:
                image[r + 1][c] = color
                queue.append([r + 1, c])
            if c > 0 and image[r][c - 1] == oldColor:
                image[r][c - 1] = color
                queue.append([r, c - 1])
            if c < len(image[r]) - 1 and image[r][c + 1] == oldColor:
                image[r][c + 1] = color
                queue.append([r, c + 1])

        image[sr][sc] = color
        getNeighborPixels(sr, sc)
        while len(queue) > 0:
            pixel = queue.pop(0)
            getNeighborPixels(pixel[0], pixel[1])

        return image

