class Solution:
    def merge_array(self, left, right):
        result = []
        i, j = 0, 0
        n, m = len(left), len(right)
        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < n:
            while i < n:
                result.append(left[i])
                i += 1
        if j < m:
            while j < m:
                result.append(right[j])
                j += 1
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        left = self.sortArray(left_nums)
        right = self.sortArray(right_nums)
        return self.merge_array(left, right)

        