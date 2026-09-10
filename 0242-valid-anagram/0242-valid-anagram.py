class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s == t
        mp = {}
        for c in s:
            if c not in mp:
                mp[c] = 0
            mp[c] += 1
        for c in t:
            if c not in mp:
                return False
            mp[c] -= 1
        for key in mp:
            if mp[key] != 0:
                return False
        return True