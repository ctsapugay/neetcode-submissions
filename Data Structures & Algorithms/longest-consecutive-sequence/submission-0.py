class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_consec = 0
        hashmap = dict()
        for num in nums:
            hashmap[num] = 1
        for num in nums:
            counter = 0
            if hashmap.get((num-1), 0) == 0:
                # can be start of sequence
                # attempt to build sequence
                counter += 1
                while (hashmap.get(num + counter, 0) != 0):
                    counter += 1
                if counter > max_consec:
                    max_consec = counter
        return max_consec
        