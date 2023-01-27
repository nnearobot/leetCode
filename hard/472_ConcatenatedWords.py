# 472. Concatenated Words
# Hard
# https://leetcode.com/problems/concatenated-words/description/

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

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dp(i, substring) -> List[int]:
            #print(i, substring)
            if not substring:
                return [0, 0]
            if len(substring) == 1 or i == len(substring) - 1:
                return [len(substring), 1] if trie.search(substring) else [0, 0]
            #print("   ", substring[:i + 1], substring[i + 1:])
            if trie.search(substring[:i + 1]):
                count = dp(0, substring[i + 1:])
                if count[0] == len(substring) - i - 1:
                    return [len(substring), count[1] + 1]
            count = dp(i + 1, substring)
            #print("   ", count, len(substring))
            return count

        res = []
        for word in words:
            count = dp(0, word)
            if count[0] == len(word) and count[1] > 1:
                res.append(word)  

        return res


