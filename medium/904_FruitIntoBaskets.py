"""
904. Fruit Into Baskets
Medium
https://leetcode.com/problems/fruit-into-baskets

"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        maxFruits = 0 
        s, newS, e = 0, 0, 0
        types = {}
        while e < len(fruits):
            if len(types) < 2 and fruits[e] not in types:
                types[fruits[e]] = 1
                newS = e
            elif fruits[e] in types:
                types[fruits[e]] += 1
                if fruits[e] != fruits[e - 1]:
                    newS = e
            else:
                for fruit in types:
                    if fruit != fruits[newS]:
                        types.pop(fruit)
                        break
                types[fruits[e]] = 1
                maxFruits = max(maxFruits, e - s)
                s = newS
                newS = e
            e += 1
        maxFruits = max(maxFruits, e - s)

        return maxFruits