class Solution:
    def binary_search(self, nums: List[int], l, r) -> int:
        # returns the first item of the second section
        if l > r:
            return 0 # not rotated

        m = (r - l) // 2 + l
        if l == m:
            return min(nums[r], nums[m])
        if nums[l] > nums[m]: # l is the odd one out
            # l < min <= m
            if nums[m-1] > nums[m]:
                return nums[m]
            return self.binary_search(nums, l, m-1)
        elif nums[m] > nums[r]: # r is the odd one out
            # m < min <= r
            return self.binary_search(nums, m+1, r)
        
        # l <= m <= r
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        return self.binary_search(nums, 0, len(nums)-1)
        