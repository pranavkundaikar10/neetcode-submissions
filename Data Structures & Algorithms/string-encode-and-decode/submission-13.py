class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while i < len(s):
            while s[j] != '#':
                j += 1
            w_len = int(s[i:j])
            i = j + 1
            word = s[i:i+w_len]
            res.append(word)
            i = i + w_len
            j = i
        return res
