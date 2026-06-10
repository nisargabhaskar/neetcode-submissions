class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for s in strs:
            hash_map = [0]*26
            for ch in s:
                hash_map[ord(ch) - ord('a')] += 1
            key = tuple(hash_map)
            hash_table[key].append(s)
            
        return list(hash_table.values())