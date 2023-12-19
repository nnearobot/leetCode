# 661. Image Smoother
# easy
# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                box_sum = img[i][j]
                box_count = 1
                if j > 0:
                    box_sum += img[i][j - 1]
                    box_count += 1
                if j < n - 1:
                    box_sum += img[i][j + 1]
                    box_count += 1

                if i > 0:
                    box_sum += img[i - 1][j]
                    box_count += 1
                    if j > 0:
                        box_sum += img[i - 1][j - 1]
                        box_count += 1
                    if j < n - 1:
                        box_sum += img[i - 1][j + 1]
                        box_count += 1
                if i < m - 1:
                    box_sum += img[i + 1][j]
                    box_count += 1
                    if j > 0:
                        box_sum += img[i + 1][j - 1]
                        box_count += 1
                    if j < n - 1:
                        box_sum += img[i + 1][j + 1]
                        box_count += 1
                res[i][j] = box_sum // box_count
        return res