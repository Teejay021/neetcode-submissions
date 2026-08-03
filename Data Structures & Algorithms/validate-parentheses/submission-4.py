class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)% 2 != 0:
            return False
            
        stack = []
        pList = dict()
        pList['('] = ')'
        pList['{'] = '}'
        pList['['] = ']'
        for paranthesis in s:
            ##it's a closing paranthesis
            if paranthesis not in pList.keys():
                if not stack:
                    return False
                
                if pList[stack.pop()] != paranthesis:
                    return False

                continue
                
            ##add the open paranthesis to the stack
            stack.append(paranthesis)

        return not stack
            