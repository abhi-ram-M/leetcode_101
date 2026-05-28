class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for num in nums:
            mapp[num] = mapp.get(num,0)+1
        heap = []
        for key, val in mapp.items():
            heapq.heappush(heap,[val,key])
            if len(heap)>k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
        
