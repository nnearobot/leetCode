/**
 * 1519. Number of Nodes in the Sub-Tree With the Same Label
 * Medium
 * https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/
 */
import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    private ArrayList<Integer>[] vertexEdges;
    private int[] subtreeLabelCount;

    public int[] countSubTrees(int n, int[][] edges, String labels) {
        subtreeLabelCount = new int[n];
        if (n == 1) {
            subtreeLabelCount[0] = 1;
            return subtreeLabelCount;
        }

        vertexEdges = new ArrayList[n];
        for (int i = 0; i < n; i++) vertexEdges[i] = new ArrayList<Integer>();
        for (int i = 0; i < edges.length; ++i) {
            vertexEdges[edges[i][0]].add(i);
            vertexEdges[edges[i][1]].add(i);
        }
        
        countSubtreeLabels(0, -1, edges, labels);

        return subtreeLabelCount;
    }

    private HashMap<Character, Integer> countSubtreeLabels(int vertexNum, int parentEdgeNum, int[][] edges, String labels) {
        HashMap<Character, Integer> labelCounts = new HashMap<Character, Integer>(),
            subTreeLabelCounts;
        Character currentLabel = labels.charAt(vertexNum),
            label;

        labelCounts.put(currentLabel, 1);

        for (int edgeNum : vertexEdges[vertexNum]) {
            if (edgeNum == parentEdgeNum) continue;

            subTreeLabelCounts = countSubtreeLabels((edges[edgeNum][0] != vertexNum ? edges[edgeNum][0] : edges[edgeNum][1]), edgeNum, edges, labels);
            for (Map.Entry<Character, Integer> labelCount : subTreeLabelCounts.entrySet()) {
                label = labelCount.getKey();
                if (!labelCounts.containsKey(label)) {
                    labelCounts.put(label, 0);
                }
                labelCounts.put(label, labelCounts.get(label) + labelCount.getValue());
            }
        }

        for (Map.Entry<Character, Integer> labelCount : labelCounts.entrySet()) {
            if (labelCount.getKey() == currentLabel) {
                subtreeLabelCount[vertexNum] = labelCount.getValue();
            }
        }

        return labelCounts;
    }
}