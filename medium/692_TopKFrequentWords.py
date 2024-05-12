# 692. Top K Frequent Words
# medium
# https://leetcode.com/problems/top-k-frequent-words

import collections
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)
        heap = [(-freq, word) for word, freq in word_counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]