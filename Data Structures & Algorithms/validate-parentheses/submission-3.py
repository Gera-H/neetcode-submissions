class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        stack = []
        setP = {}
        setP[']'] = '['
        setP['}'] = '{'
        setP[')'] = '('

        stack.append(s[0])
        for i in range(1,len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if s[i] in setP:
                if setP[s[i]] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(s[i])
        return not bool(stack)