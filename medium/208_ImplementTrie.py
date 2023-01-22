"""
208. Implement Trie (Prefix Tree)
Medium
https://leetcode.com/problems/implement-trie-prefix-tree/description/

"""

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

    def search(self, word: str) -> bool:
        node = self.root
        for l in word:
            if l not in node.children:
                return False
            node = node.children[l]
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for l in prefix:
            if l not in node.children:
                return False
            node = node.children[l]
        return True