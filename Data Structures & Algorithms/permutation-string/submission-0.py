class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for i in s1:
            seen[i] = seen.get(i,0) + 1
        
        l, r = 0, 0

        while r < len(s2):
            
            current_window_length = r - l + 1


            if current_window_length > len(s1):
                seen[s2[l]] += 1
                l += 1


            
            if s2[r] in seen:
                seen[s2[r]] -= 1
                if r - l + 1 == len(s1) and all(value == 0 for value in seen.values()):
                    return True 
                r +=1
            else: 
                while l < r:
                    seen[s2[l]] += 1
                    l += 1
                r += 1
                l +=1
                    
            
        return False


