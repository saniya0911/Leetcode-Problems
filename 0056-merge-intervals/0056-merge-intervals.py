class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        n = len(intervals)
        ans = []
        prev = intervals[0]
        for i in range(1, n):
            if intervals[i][0] <= prev[1]:
                prev = [prev[0], max(prev[1], intervals[i][1])]
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans
