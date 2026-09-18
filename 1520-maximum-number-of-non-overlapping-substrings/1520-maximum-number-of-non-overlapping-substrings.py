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

        right = -1
        ans = []
        for i in range(n):
            ch = s[i]
            start = indices[ch]['start']
            end = indices[ch]['end']
            if i == start:
                j = i
                valid = True
                while j <= end:
                    curr = s[j]
                    if indices[curr]['start'] < start:
                        valid = False
                        break
                    end = max(end, indices[curr]['end'])
                    j += 1

                if valid:
                    if i > right:
                        ans.append(s[start: end+1])
                    else:
                        ans[-1] = s[start:end+1]
                    right = end
            
        return ans
                    
        
        # intervals = []
        # s1 = set(s)
        # for ch in s1:
        #     start = indices[ch]['start']
        #     end = indices[ch]['end']
        #     valid = True
        #     i = start

        #     while i <= end:
        #         curr = s[i]
        #         if indices[curr]['start'] < start:
        #             valid = False
        #             break
                
        #         end = max(end, indices[curr]['end'])
        #         i += 1
            
        #     if valid:
        #         intervals.append([start, end])
        
        # intervals.sort(key = lambda x: (x[1], x[1] - x[0]))
        # ans = []
        # prev_end = -1
        # for start, end in intervals:
        #     if start > prev_end:
        #         ans.append(s[start: end+1])
        #         prev_end = end
        
        # return ans