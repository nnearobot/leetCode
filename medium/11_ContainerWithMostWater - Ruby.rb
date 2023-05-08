# 11. Container With Most Water
# Medium
# https://leetcode.com/problems/container-with-most-water/

# @param {Integer[]} height
# @return {Integer}
def max_area(height)
    max_vol = 0
    point1 = 0
    point2 = height.length() - 1
    while point1 < point2
        vol = [height[point1], height[point2]].min * (point2 - point1)
        max_vol = [vol, max_vol].max
        if height[point1] < height[point2]
            point1 += 1
        else
            point2 -= 1
        end
    end

    return max_vol
end
