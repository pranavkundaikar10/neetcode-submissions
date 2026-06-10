class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {'}': '{', ']':'[', ')':'('}
        i, stack = 0, []
        while i < len(s):
            if s[i] in bmap.keys():
                if not stack or stack[-1] != bmap.get(s[i], ""):
                    return False
                stack.pop()
            else:
                stack.append(s[i])
            i += 1

        if stack:
            return False
        return True