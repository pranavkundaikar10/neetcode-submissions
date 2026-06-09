class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True


    def isAlphaNum(self, val):
        return (
            ((ord('a') <= ord(val)) and (ord(val) <= ord('z'))) or
            ((ord('A') <= ord(val)) and (ord(val) <= ord('Z'))) or
            ((ord('0') <= ord(val)) and (ord(val) <= ord('9')))
            )