class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for element in nums:
            try:
                i = hashmap[element]
                return True
            except:
                hashmap[element] = 1;
        return False
        