// 1207. Unique Number of Occurrences
// easy
// https://leetcode.com/problems/unique-number-of-occurrences

use std::collections::HashMap;

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut numMap: HashMap<i32, u32> = HashMap::new();
        for num in arr {
            *numMap.entry(num).or_insert(0) += 1;
        }
        let mut countMap: Vec<&u32> = numMap.values().collect();
        countMap.sort();
        let mut prev = &countMap[0];
        for count in &countMap[1..] {
            if (count == prev) {
                return false;
            }
            prev = count;
        }

        true
    }
}