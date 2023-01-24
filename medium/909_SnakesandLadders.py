"""
909. Snakes and Ladders
Medium
https://leetcode.com/problems/snakes-and-ladders/

"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [0]
        for row in range(n):
            arr = range(n) if row % 2 == 0 else reversed(range(n))
            for col in arr:
                cells.append(board[n - row - 1][col])
 
        children = [set()]
        for x in range(len(cells)):
            if x == 0:
                continue
            children.append(set())
            for i in range(min(6, len(cells) - x - 1)):
                nextCell = x + i + 1
                if cells[nextCell] == -1:
                    children[x].add(nextCell)
                else:
                    children[x].add(cells[nextCell])

        steps = n * n
        pathLengths = {}

        def dfs(curCell, prevSteps):
            nonlocal steps
            prevSteps += 1

            if curCell in pathLengths:
                if prevSteps >= pathLengths[curCell]:
                    return
            pathLengths[curCell] = prevSteps

            if len(children[curCell]) == 0:
                steps = min(steps, prevSteps)
                return

            for nextCell in children[curCell]:
                dfs(nextCell, prevSteps)                                     

        dfs(1, -1)

        return -1 if steps == n * n else steps

