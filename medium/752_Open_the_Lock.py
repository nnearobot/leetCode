# 752. Open the Lock
# medium
# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        visited = set()
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        q = collections.deque()
        q.append((0, 0, 0, 0, 0))
        res = -1
        while len(q):
            a, b, c, d, prev_count = q.popleft()
            number = digits[a] + digits[b] + digits[c] + digits[d]
            if number in deadends_set:
                continue
            if number in visited:
                continue
            visited.add(number)
            if number == target:
                res = prev_count if res == -1 else min(res, prev_count)
                continue
            #print(number, prev_count)
            params = [
                ((a + 1) % 10, b, c, d),
                ((a - 1) % 10, b, c, d),
                (a, (b + 1) % 10, c, d),
                (a, (b - 1) % 10, c, d),
                (a, b, (c + 1) % 10, d),
                (a, b, (c - 1) % 10, d),
                (a, b, c, (d + 1) % 10),
                (a, b, c, (d - 1) % 10),
            ]
            for param in params:
                q.append((*param, prev_count + 1))

        return res
