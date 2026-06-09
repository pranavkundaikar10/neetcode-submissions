class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i, j, res = 0, 0, 0
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            res = max(res, len(s[i:j])+1)
            j += 1

        return res            
        