# 1268. Search Suggestions System
# medium
# https://leetcode.com/problems/search-suggestions-system

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products) - 1
        result = []

        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1
            while l <= r and (len(products[l]) <= i or products[r][i] != searchWord[i]):
                r -= 1

            remain = r - l + 1
            if remain < 1:
                result.append([])
            else:
                result.append(products[l:l + min(3, remain)])

        return result
