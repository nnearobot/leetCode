// 958. Check Completeness of a Binary Tree
// medium
// https://leetcode.com/problems/check-completeness-of-a-binary-tree

package main
import (
	"container/list"
	"math"
)

type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
}

type nodeTrio struct {
    Node *TreeNode
    Lvl  int
	Left bool
}

func isCompleteTree(root *TreeNode) bool {
	q := list.New()
	q.PushBack(nodeTrio{Node: root, Lvl: 0, Left: true})

	curLvl, count := 0, 0
	prevLeft := false
	for q.Len() > 0 {
		front := q.Front()
		trio := front.Value
		q.Remove(front)

		if trio.Lvl == curLvl {
			count++
			if trio.Left == prevLeft {
				return false
			}
		} else {
			if float64(count) < math.Pow(2, float64(curLvl)) {
				return false
			}
			curLvl++
			count = 1
			prevLeft = true
		}

		if trio.Node.Left != nil {
			q.PushBack(nodeTrio{Node: trio.Node.Left, Lvl: curLvl + 1, Left: true})
		}
		if trio.Node.Left != nil {
			q.PushBack(nodeTrio{Node: trio.Node.Left, Lvl: curLvl + 1, Left: false})
		}
	}

	return true
}