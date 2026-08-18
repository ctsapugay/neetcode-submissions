class Solution:
    def binary_search(self, nums: List[int], target: int, l, r) -> int:
        if l > r:
            return -1
        m = r - l // 2 + l
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binary_search(nums, target, m+1, r)
        return self.binary_search(nums, target, l, r-1)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)

        