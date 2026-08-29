class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        while l < len(prices):
            r = min(l+1, len(prices)-1)
            while r < len(prices):
                res = max(res, prices[r]-prices[l])
                r += 1
            l += 1

        return res
            