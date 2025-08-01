class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, low, high, target):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(nums, mid + 1, high, target)
            else:
                return binary_search(nums, low, mid - 1, target)
        
        return binary_search(nums, 0, len(nums) - 1, target)
