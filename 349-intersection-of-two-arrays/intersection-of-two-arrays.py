class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if 1<= len(nums1) <= 1000 and 1<= len(nums1) <= 1000:
            result = []
            nums1_set = set(nums1)
            for i in nums1_set:
                if i in nums2:
                    result.append(i)
            return result