class MedianFinder:

    def __init__(self):
        # self.arr = SortedList()
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # self.arr.add(num)
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self) -> float:
        # n = len(self.arr)
        # if n%2 == 0:
        #     return (self.arr[n//2] + self.arr[n//2-1])/2
        # return self.arr[n//2]
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()