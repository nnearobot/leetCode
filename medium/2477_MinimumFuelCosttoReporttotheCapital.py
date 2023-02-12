# 2477. Minimum Fuel Cost to Report to the Capital
# Medium
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital
import collections

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = collections.defaultdict(list)
        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])
        peopleFromCity = collections.defaultdict(int)
        def getCityCount(city, prevCity) -> int:
            if city not in peopleFromCity:
                peopleFromCity[city] = 0
            if len(adj[city]) == 1:
                peopleFromCity[city] = 1
                return 1
            count = 1
            for neighCity in adj[city]:
                if neighCity == prevCity:
                    continue
                count += getCityCount(neighCity, city)
            peopleFromCity[city] += count
            return count
        for city in adj[0]:
            getCityCount(city, 0)
        res = 0
        for city in peopleFromCity:
            res += math.ceil(peopleFromCity[city] / seats)
        
        return res
