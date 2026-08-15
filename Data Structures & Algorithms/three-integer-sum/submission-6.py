class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums)-2:
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                i  +=1
                continue
            l = i+1
            r = len(nums) -1
            tmp = 0 - nums[i]
            while l < r:
                threeSum = nums[l] + nums[r]
                if threeSum > tmp:
                    r -=1
                elif threeSum < tmp:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            i +=1
        
        return res