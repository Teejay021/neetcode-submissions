class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        counts1 = {}
        counts2 ={}
        for w in s:
            counts1[w] = counts1.get(w, 1) + 1

        for w in t:
            counts2[w] = counts2.get(w, 1) + 1

        return counts1 == counts2
