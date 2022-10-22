/**
 * 104. Maximum Depth of Binary Tree
 * Easy
 * Given the root of a binary tree, return its maximum depth.
 *
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
	return getDepth(root, 0)
}

func getDepth(root *TreeNode, depth int) int {
	if root == nil {
		return depth
	}

	depth++

	newDepthLeft, newDepthRight := 0, 0
	if root.Left != nil {
		newDepthLeft = getDepth(root.Left, depth)
	}

	if root.Right != nil {
		newDepthRight = getDepth(root.Right, depth)
	}

	if newDepthLeft > depth {
		depth = newDepthLeft
	}
	if newDepthRight > depth {
		depth = newDepthRight
	}

	return depth
}
