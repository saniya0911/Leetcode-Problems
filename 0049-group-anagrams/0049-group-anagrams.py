class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            ss = "".join(sorted(s))
            if ss in hashmap:
                hashmap[ss].append(s)
            else:
                hashmap[ss] = [s]

        ans = []
        for value in hashmap.values():
            ans.append(value)
        
        return ans