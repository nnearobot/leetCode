/**
 * 1443. Minimum Time to Collect All Apples in a Tree
 * Medium
 * https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
 */
import java.util.HashSet;
import java.util.ArrayList;

class Solution {
    private HashSet<Integer> visitedEdges = new HashSet<Integer>();
    private int[][] edgeList;
    private ArrayList<Integer>[] vertexParentEdges;

    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        if (n == 1) {
            return 0;
        }

        edgeList = edges;
        vertexParentEdges = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            vertexParentEdges[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < edgeList.length; ++i) {
            vertexParentEdges[edgeList[i][0]].add(i);
            vertexParentEdges[edgeList[i][1]].add(i);
        }
        
        for (int i = 1; i < hasApple.size(); ++i) {
            if (hasApple.get(i) == false) {
                continue;
            }

            checkPath(i, -1);
        }

        return visitedEdges.size() * 2;
    }

    private Boolean checkPath(int vertexNum, int edgeNum) {
        if (vertexNum == 0) {
            return true;
        }

        for (int i : vertexParentEdges[vertexNum]) {
            if (edgeNum == i) {
                continue;
            }

            if (visitedEdges.contains(i)) {
                return true;
            }

            if (checkPath((edgeList[i][0] != vertexNum ? edgeList[i][0] : edgeList[i][1]), i)) {
                visitedEdges.add(i);
                return true;
            }
        }

        return false;
    }
}