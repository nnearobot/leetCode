/**
 * 1137. N-th Tribonacci Number
 * Easy
 * The Tribonacci sequence Tn is defined as follows: 
 * T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
 * Given n, return the value of Tn.
 */
class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        
        int n0 = 0;
        int n1 = 1;
        int n2 = 1;
        int res = 0;
        
        for (int i = 3; i <= n; i++) {
            res = n0 + n1 + n2;
            n0 = n1;
            n1 = n2;
            n2 = res;
        }
        
        return res;
    }
}