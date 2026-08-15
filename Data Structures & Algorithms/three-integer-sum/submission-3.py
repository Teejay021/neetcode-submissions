class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        i = 0
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i  +=1
                continue
            l = i+1
            r = len(nums) -1
            tmp = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] > tmp:
                    r -=1
                elif nums[l] + nums[r] < tmp:
                    l += 1
                else:
                    triplet = [nums[i],nums[l],nums[r]]
                    if triplet not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -=1
            i +=1
        
        return res