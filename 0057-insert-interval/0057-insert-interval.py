class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        if n == 0:
            ans.append(newInterval)
            return ans
        if n==1:
            if newInterval[0] < intervals[0][0]:
                ans.append(newInterval)
                ans.append(intervals[0])
                return self.mergeinterval(ans)
            else:
                ans.append(intervals[0])
                ans.append(newInterval)
                return self.mergeinterval(ans)
            
        inserted = False
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                ans.append(newInterval)
                inserted = True
                break
            else:
                ans.append(intervals[i])
        
        if not inserted:
            ans.append(newInterval)

        while not (len(ans) >= n+1):
            ans.append(intervals[i])
            i += 1
        return self.mergeinterval(ans)

    def mergeinterval(self, intervals):
        n = len(intervals)
        prev = intervals[0]
        ans = []
        for i in range(1, n):
            if intervals[i][0] <= prev[1]:
                prev = [prev[0], max(prev[1], intervals[i][1])]
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans
