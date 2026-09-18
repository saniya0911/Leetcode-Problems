class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        indices = {}
        n = len(s)
        for i in range(n):
            if s[i] not in indices:
                indices[s[i]] = {
                    'start': i,
                    'end': i,
                    'f': 1
                }
            else:
                indices[s[i]]['end'] = i
                indices[s[i]]['f'] += 1
        
        intervals = []
        s1 = set(s)
        for ch in s1:
            start = indices[ch]['start']
            end = indices[ch]['end']
            valid = True
            i = start

            while i <= end:
                curr = s[i]
                if indices[curr]['start'] < start:
                    valid = False
                    break
                
                end = max(end, indices[curr]['end'])
                i += 1
            
            if valid:
                intervals.append([start, end])
        
        intervals.sort(key = lambda x: x[1])
        ans = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start: end+1])
                prev_end = end
        
        return ans