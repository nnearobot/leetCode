'''
1626. Best Team With No Conflicts
Medium
https://leetcode.com/problems/best-team-with-no-conflicts/description/

'''
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        if len(scores) == 1:
            return scores[0]

        players = [(ages[i], scores[i]) for i in range(len(scores))]
        players = sorted(players, key = lambda i: (i[0], i[1]))

        dp = [player[1] for player in players]
        res = 0
        for x in range(len(players) - 1):
            i = x + 1
            for j in range(i - 1, -1, -1):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], players[i][1] + dp[j])
            res = max(res, dp[i])

        return res

