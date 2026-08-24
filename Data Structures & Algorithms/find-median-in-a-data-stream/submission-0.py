class MedianFinder:

    def __init__(self):
        self.max_heap = []  # lower half
        self.min_heap = []  # upper half
        self.length = 0

    def addNum(self, num: int) -> None:
        if len(self.max_heap) < 1 and len(self.min_heap) < 1:
            heapq.heappush_max(self.max_heap, num)
        elif num < self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)
        
        difference = len(self.max_heap) - len(self.min_heap)
        if difference > 1:
            # max heap has at least 2 more
            item = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, item)
        elif difference < -1:
            # min heap has at least 2 more
            item = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, item)

        self.length += 1
        return

    def findMedian(self) -> float:
        print(self.length)
        if self.length % 2:  # if odd
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            return self.max_heap[0]
        return (self.min_heap[0] + self.max_heap[0]) / 2