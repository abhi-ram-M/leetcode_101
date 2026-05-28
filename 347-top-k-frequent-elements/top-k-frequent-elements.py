# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         mapp = {}
#         for num in nums:
#             mapp[num] += 1
#         heap = []
#         for key,val in mapp.items:
           
#             if len(heap) < 2:
#                 heap.heappush(heap,[val,key])
#             if len(heap)>2:
#                 heap.heappop(heap)         
#         return [i[1] for i in heap]
        
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}

        # Count frequencies
        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1

        heap = []

        # Maintain a min-heap of size k
        for key, val in mapp.items():

            if len(heap) < k:
                heapq.heappush(heap, [val, key])
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [val, key])

        return [i[1] for i in heap]