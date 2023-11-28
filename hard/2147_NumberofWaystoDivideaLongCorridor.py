# 2147. Number of Ways to Divide a Long Corridor
# Hard
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        number_of_ways = 1
        all_seats = 0
        dividers = 1
        modulo = 1000000007
        for letter in corridor:
            if letter == 'S':
                all_seats += 1
                if dividers > 1:
                    tmp = 0
                    for i in range(dividers):
                        tmp += number_of_ways
                        if tmp >= modulo:
                            tmp -= modulo
                    number_of_ways = tmp
                    dividers = 1
            elif all_seats > 0 and all_seats % 2 == 0:
                    dividers += 1

        return 0 if all_seats == 0 or all_seats % 2 == 1 else number_of_ways

