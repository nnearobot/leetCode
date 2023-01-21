"""
93. Restore IP Addresses
Medium
https://leetcode.com/problems/restore-ip-addresses/description/

"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        sList = [int(x) for x in list(s)]
        res = []
        ipArr = []

        def backtrack(i, curInt):
            if i == len(sList):
                if len(ipArr) == 4 and not curInt:
                    string_list = [str(x) for x in ipArr]
                    res.append(".".join(string_list))
                return

            if (curInt):
                curInt = curInt * 10 + sList[i]
            else:
                curInt = sList[i]

            if curInt > 255:
                return

            # dont put the dot after ith digit
            if curInt != 0 and curInt <= 25:
                backtrack(i + 1, curInt)

            # put the dot after ith digit
            ipArr.append(curInt)
            backtrack(i + 1, None)
            ipArr.pop() #this is a backtrack

        backtrack(0, None)

        return res


