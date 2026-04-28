class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        sol =[]

        for key, value in sorted_dict:
            if k == 0:
                break
            sol.append(key)
            k -= 1
                

        return sol