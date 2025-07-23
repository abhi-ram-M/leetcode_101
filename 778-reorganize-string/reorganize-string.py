class Solution:
    def reorganizeString(self, s: str) -> str:
        if (1 <= len(s) <= 500):
            import heapq
            res = []
            char_count = {}
            for char in s:
                char_count[char] = char_count.get(char,0)+1
            max_heap = []
            for k,v in char_count.items():
                if v > (len(s)+1)//2:
                    return ''
                max_heap.append([-v,k])
            heapq.heapify(max_heap)
            prev_count,prev_value = 0,''
            while max_heap:
                curr_count,curr_value = heapq.heappop(max_heap)
                res.append(curr_value)
                if prev_count < 0:
                    heapq.heappush(max_heap,[prev_count,prev_value])
                prev_count,prev_value = curr_count+1,curr_value
            
            return ''.join(res)








            

            