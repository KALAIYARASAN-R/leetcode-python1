class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        merge = ''

        for i in range(min(l1, l2)):
            merge += word1[i]
            merge += word2[i]
        
        merge += word1[l2:] if l1 > l2 else word2[l1:]

        return merge