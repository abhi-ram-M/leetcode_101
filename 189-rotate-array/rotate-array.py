class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if (1 <= n <= 10**5) and (0 <= k <= 10**5):
            k = k%n
            if n>1:
                nums[:] = nums[-k:]+nums[:-k]
        