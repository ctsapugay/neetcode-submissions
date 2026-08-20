class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        max_heap = [-c for c in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # [-freq, time available]
        
        while max_heap or q:
            time += 1

            if max_heap:
                c = heapq.heappop(max_heap) + 1
                if c: q.append([c, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time