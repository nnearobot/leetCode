/**
 * 134. Gas Station
 * Medium
 * https://leetcode.com/problems/gas-station/
 */

class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;

        int total = 0, current = 0, start = 0;
        for (int i = 0; i < n; ++i) {
            total += gas[i] - cost[i];
            current += gas[i] - cost[i];
            if (current < 0) {
                start = i + 1;
                current = 0;
            }
        }
        return total >= 0 ? start : -1;
    }
}

// import java.util.Arrays;

// class Solution {
//     public int canCompleteCircuit(int[] gas, int[] cost) {
//         int gasSum = Arrays.stream(gas).sum();
//         int costSum = Arrays.stream(cost).sum();

//         if (gasSum < costSum) {
//             return -1;
//         }

//         for (int i = 0; i < gas.length; i++) {
//             if (gas[i] == 0 || gas[i] < cost[i]) {
//                 continue;
//             }
//             int j = i;
//             int tank = gas[j];
//             while (true) {
//                 tank -= cost[j];
//                 if (tank < 0) {
//                     break;
//                 }

//                 j++;
//                 if (j >= gas.length) {
//                     j = 0;
//                 }

//                 if (j == i) {
//                     return i;
//                 }

//                 tank += gas[j];
//             };
//         }

//         return -1;
//     }
// }