class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dic = {}
        res = []
        for i in range (len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in my_dic:
                my_dic[sorted_word].append(i)
                continue
            my_dic[sorted_word] = [i]
        
        for key,value in my_dic.items():
            sol = []
            for i in range(len(value)):
                sol.append(strs[value[i]])
            res.append(sol)
        

        return res

        