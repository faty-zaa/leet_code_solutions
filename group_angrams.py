from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        names = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            names[key].append(word)
        return (list(names.values()))
            