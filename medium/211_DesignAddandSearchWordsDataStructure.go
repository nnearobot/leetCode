// 211. Design Add and Search Words Data Structure
// Medium
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

package main

import "fmt"

type WordDictionary struct {
	root *WordNode
}

type WordNode struct {
	isWord   bool
	children map[rune]*WordNode
}

func Constructor() WordDictionary {
	return WordDictionary{root: &WordNode{children: make(map[rune]*WordNode)}}
}

func (this *WordDictionary) AddWord(word string) {
	current := this.root
	for _, runeVal := range word {
		if _, ok := current.children[runeVal]; !ok {
			current.children[runeVal] = &WordNode{children: make(map[rune]*WordNode)}
		}
		current = current.children[runeVal]
	}
	current.isWord = true
}

func (this *WordDictionary) Search(word string) bool {
	return searchInNode(word, this.root)
}

func searchInNode(word string, node *WordNode) bool {
	for i, runeVal := range word {
		child, ok := node.children[runeVal]
		if !ok {
			if runeVal == '.' {
				for _, child := range node.children {
					if searchInNode(word[i+1:], child) {
						return true
					}
				}
			}
			return false
		} else {
			node = child
		}
	}

	return node.isWord
}

func main() {
	obj := Constructor()
	obj.AddWord("bad")
	obj.AddWord("mad")
	obj.AddWord("dad")

	fmt.Println(obj.Search("pad"))
	fmt.Println(obj.Search("sad"))
	fmt.Println(obj.Search("bad"))
	fmt.Println(obj.Search(".ad"))
	fmt.Println(obj.Search("..d"))
	fmt.Println(obj.Search("ma."))
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */

/**
{false map[
    98:{false map[
        97:{false map[
            100:{false map[]}
            ]}
        ]}
    100:{false map[
        97:{false map[
            100:{false map[]}
            ]}
        ]}
    109:{false map[
        97:{false map[
            100:{false map[]}
            ]}
        ]}
    ]
}
 **/
