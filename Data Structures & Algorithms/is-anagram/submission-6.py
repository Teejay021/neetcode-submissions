class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        counts1 = {}
        counts2 ={}
        for i in range(len(s)):
            counts1[s[i]] = counts1.get(s[i], 0) + 1
            counts2[t[i]] = counts2.get(t[i], 0) + 1

        return counts1 == counts2
