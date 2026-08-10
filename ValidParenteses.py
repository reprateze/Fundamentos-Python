class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in mapping:
                if not stack:
                    return False
                
                top = stack.pop()   

                if mapping[i] != top:
                    return False
            else:
                stack.append(i)

        return not stack