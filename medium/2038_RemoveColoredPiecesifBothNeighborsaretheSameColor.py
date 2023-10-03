# 2038. Remove Colored Pieces if Both Neighbors are the Same Color
# medium
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False

        a, b, count = 0, 0, 1
        n = len(colors)
        for i in range(1, n + 1):
            print(colors[i - 1], a, b, count)
            if i < n and colors[i] == colors[i - 1]:
                count += 1
                continue

            if count < 3:
                count = 1
                continue

            if colors[i - 1] == 'A':
                a += count - 2
            else:
                b += count - 2
            count = 1        
        
        return a > b        
