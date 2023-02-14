# 67. Add Binary
# Easy
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #return '{0:b}'.format(int(a, 2) + int(b, 2))

        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
            #print(x, y, bin(x))
        return bin(x)[2:]

        '''
        res = ""
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        print(a, b)
        add = "0"

        for i in range(n - 1, -1, -1):
            tmp = add
            if a[i] == "1" and b[i] == "1":
                tmp = "1" if add == "1" else "0"
                add = "1"
            elif a[i] == "1" or b[i] == "1":
                tmp = "1" if add == "0" else "0"
            else:
                add = "0"
            res = tmp + res
        
        if add == "1":
            res = add + res

        return res
        '''

