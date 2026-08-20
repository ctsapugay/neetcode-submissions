class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        frequencies = {}
        for t in tasks:
            frequencies[t] = frequencies.get(t, 0) + 1

        max_heap = []
        for char, freq in frequencies.items():
            heapq.heappush_max(max_heap, [freq, char])

        cooldown = deque()
        for i in range(n+1):
            cooldown.append([-1, "-"])

        cd_len = 0
        while len(max_heap) > 0 or cd_len > 0:
            # print(max_heap)
            # print(cooldown)
            # 1. process cool down item
            item = cooldown.popleft()
            if item[0] > 0:
                heapq.heappush_max(max_heap, item)
                cd_len -= 1
            # print(cooldown)
            # print(max_heap)
            # print(" -------------------")
        # add items with freq > 0 to the heap
        # if item were to have 0 freq we are 
        # not to add it to the queue   

        # process heap item, or empty, append idle time
            if len(max_heap) > 0:
                item = heapq.heappop_max(max_heap)
                item[0] -= 1
                if item[0] < 1:
                    cooldown.append([-1, "-"]) 
                else:
                    cooldown.append(item)
                    cd_len += 1 
            else:
                cooldown.append([-1, "-"]) 
            
            time += 1

        return time