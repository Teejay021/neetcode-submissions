class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #how does organizing help with the solution?
        # getting the smallest element?
        # where does binary search come into help?
        # 9 / 2 = 4 -> mean anything?
        # 1,4,3,2
        # num - k and while > 0 then we keep adding to hours
        # to get the minimumm we know fastest way is the maximum which means
        # it would finish in len(piles) so that is the ceiling
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r)// 2
            hours = 0
            for p in piles:
                hours += math.ceil(p /k)
            if hours <= h:
                res = min(res,k)
                r = k-1
            else: 
                l = k+1
        
        return res