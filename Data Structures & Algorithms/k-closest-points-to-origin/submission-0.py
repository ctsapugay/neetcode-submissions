class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for pt in points:
            x,  y = pt[0], pt[1]
            dist = x**2 + y**2
            heapq.heappush_max(heap, [dist, x, y])
        
        print(heap)
        while len(heap) > k:
            heapq.heappop_max(heap)
        
        while len(heap) > 0:
            dist, x, y = heapq.heappop_max(heap)
            result.append([x, y])
        
        return result