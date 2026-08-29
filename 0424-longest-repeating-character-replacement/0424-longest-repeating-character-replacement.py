class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        start = 0
        total_max = 0
        freq = {}
        for end in range(len(s)):
            ch = s[end]
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

            w = end - start + 1
            if w - max(freq.values()) <= k:
                total_max = max(total_max, w)
            else:
                freq[s[start]] -= 1
                start += 1
        return total_max
                    


            
