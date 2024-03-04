# 948. Bag of Tokens
# medium
# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        scores = 0
        left = 0
        right = len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                scores += 1
                power -= tokens[left]
                left += 1
            elif left < right and scores > 0:
                scores -= 1
                power += tokens[right]
                right -= 1
            else:
                return scores
        
        return scores
