# 1065. Index Pairs of a String
# Easy
# https://leetcode.com/problems/index-pairs-of-a-string/description/

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.isWord = True    

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for i in range(len(text)):
            s = trie.root
            for j in range(i, len(text)):
                if text[j] not in s.children:
                    break
                s = s.children[text[j]]
                if s.isWord:
                    res.append([i, j])
        return res
