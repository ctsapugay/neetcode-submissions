class Solution:
    def find_cut(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minidx = 0

        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                if nums[l] < nums[minidx]:
                    minidx = l
                l = m + 1
            else:
                if nums[m] < nums[minidx]:
                    minidx = m
                r = m - 1
            
        return minidx

    def binary_search(self, nums: List[int], target: int, l, r) -> int:
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        cut = self.find_cut(nums)

        out = self.binary_search(nums, target, 0, cut - 1)
        if out != -1:
            return out
        return self.binary_search(nums, target, cut, len(nums) - 1)
        
        