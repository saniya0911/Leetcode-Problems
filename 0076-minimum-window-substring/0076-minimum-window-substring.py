class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m<n:
            return ""

        mp = dict()
        for c in t:
            if c in mp:
                mp[c] +=1
            else:
                mp[c] = 1

        count = n
        start = 0
        min_length = m + 1
        left = 0
        right = 0
        while right < m:
            if s[right] in mp:
                if mp[s[right]] > 0:
                    count -= 1
                mp[s[right]] -= 1

            while count == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                if s[left] in mp:
                    mp[s[left]] += 1
                    if mp[s[left]] > 0:
                        count += 1

                left += 1
            right += 1

        if min_length == m+1:
            return ""
        print(min_length)

        return s[start: start + min_length]