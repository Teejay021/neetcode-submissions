class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        answ = 0
        for num in nums:
            length = 0
            if (num-1) not in seen:
                curr = num
                while curr in seen:
                    length += 1
                    curr +=1
                if length > answ:
                    answ = length

        return answ