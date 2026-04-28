class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for p in s:
            if p not in mapping:
                stack.append(p)
            else:
                if not stack or stack[-1] != mapping[p]:
                    return False
                stack.pop()

        return True if not stack else False