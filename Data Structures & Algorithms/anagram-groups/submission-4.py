class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anMap = defaultdict(list)
        for st in strs:
            ctr = [0] * 26
            for i in st:
                ctr[ord(i)-ord('a')] += 1
            anMap[tuple(ctr)].append(st)
        return list(anMap.values())


        