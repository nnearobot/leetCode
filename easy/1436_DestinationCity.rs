// 1436. Destination City
// easy
// https://leetcode.com/problems/destination-city/

use std::collections::HashMap;

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let mut from_map: HashMap<String, bool> = HashMap::new();
        for path in paths {
            from_map.entry(path[0].clone()).and_modify(|e| {*e = true}).or_insert(true);
            from_map.entry(path[1].clone()).or_insert(false);
        }
        for (city, paths_from) in from_map {
            if !paths_from {
                return city;
            }
        }
        return "".to_string();
    }
}