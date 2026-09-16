class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #what condition would make us move the pointers something to think about
        #the condition is seeing a letter that is not in the hashset perhaps
        #so then we move the left pointer perhaps
        seen = {}
        for c in s1:
            seen[c] = seen.get(c,0) +1
        
        size = len(s1)
        l,r = 0,0
        count = seen.copy()
        while r < len(s2):
            if s2[r] in seen:
                count[s2[r]] -= 1
                r +=1 
            else:
                count = seen.copy()
                r += 1
                l = r

            window_length = r -l
            
            if window_length == size: # window lenght is equal or bigger
                #check if all counts in the hashmap is zero if yes return t
                #don't know how to do that
                
                if all(value == 0 for value in count.values()):
                    return True

                else:
                    count[s2[l]] += 1
                    l += 1

        return False

                        

