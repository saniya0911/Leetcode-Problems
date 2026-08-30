class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key = lambda x: x[0])
    #     count = self.solve(intervals, 0, [-inf, -inf])
    #     return count

    # def solve(self, intervals, index, prev):
    #     if not intervals or len(intervals) == 1 or len(intervals) <= index:
    #         return 0

    #     take = inf
    #     if intervals[index][0] >= prev[1]:
    #         take = self.solve(intervals, index+1, intervals[index])
    #     dont_take = 1 + self.solve(intervals, index+1, prev)

    #     return min(take, dont_take)

        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        prev = 0
        count = 1
        for index in range(1, n):
            if intervals[index][0] >= intervals[prev][1]:
                prev = index
                count += 1
        return n - count