"""
1061. Lexicographically Smallest Equivalent String
Medium
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

"""

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        dctnry = {}
        for i, l1 in enumerate(s1):
            l2 = s2[i]
            v1 =  dctnry.get(l1, l1)
            v2 = dctnry.get(l2, l2)
            l = min(l1, l2, v1, v2)
            if l in dctnry:
                l = dctnry[l]
            dctnry[l1] = l
            dctnry[l2] = l
            for k in list(dctnry):
                v = dctnry[k]
                if v != l and (v == v1 or v == v2):
                    dctnry[k] = l
        print(dctnry)
        res = ""
        for l in baseStr:
            res += dctnry.get(l, l)
        
        return res
