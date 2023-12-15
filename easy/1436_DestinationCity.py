# 1436. Destination City
# easy
# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fromMap = collections.defaultdict(int)
        for path in paths:
            fromMap[path[0]] += 1
            fromMap[path[1]] += 0
        print(fromMap)
        for (city, pathsFrom) in fromMap.items():
            if pathsFrom == 0:
                return city
        return ""