# 2225. Find Players With Zero or One Losses
# medium
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_players = collections.defaultdict(int)
        for match in matches:
            lost_players[match[0]] += 0
            lost_players[match[1]] += 1
        return [
            sorted([i for i, v in lost_players.items() if v == 0]),
            sorted([i for i, v in lost_players.items() if v == 1])
        ]
