class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if 0 <= n <= 10**5:
            low = 0
            high = n-1
            first,last = -1,-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    last,first = mid,mid
                    while last<n-1 and (nums[last] == nums[last+1]):
                        last += 1
                    while first>=1 and (nums[first] == nums[first-1]):
                        first -= 1
                    return [first,last]
                elif nums[mid]<target:
                    low = mid+1
                else:
                    high = mid - 1
            return [first,last]
