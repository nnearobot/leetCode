# 1675. Minimize Deviation in Array
# Hard
# https://leetcode.com/problems/minimize-deviation-in-array

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        oddMax = 0
        evenMin = math.inf
        q = []
        for num in nums:
            if num % 2 == 1:
                oddMax = max(oddMax, num)
                heapq.heappush(q, -num * 2)
            else:
                evenMin = min(evenMin, num)
                heapq.heappush(q, -num)

        dev = math.inf
        minVal = -max(q)
        while True:
            maxVal = -heapq.heappop(q)
            dev = min(dev, maxVal - minVal)
            print(maxVal, minVal, dev)
            if maxVal % 2 == 0:
                val = maxVal // 2
                minVal = min(minVal, val)
                heapq.heappush(q, -val)
            else:
                break

        return dev
