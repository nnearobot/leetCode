package easy

// Returns indices of the two numbers such that they add up to target.
func TwoSum(nums []int, target int) []int {
	var numMap = map[int]int{}
	var num int

	for i := 0; i < len(nums); i++ {
		num = target - nums[i]
		if val, ok := numMap[num]; ok {
			return []int{val, i}
		}

		numMap[nums[i]] = i
	}

	return []int{}
}
