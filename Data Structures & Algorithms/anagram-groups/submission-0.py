class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            temp[sorteds].append(s)
        return list(temp.values())
