class Solution:
    def reorganizeString(self, s: str) -> str:
        if (1 <= len(s) <= 500):
            import heapq
            char_count = {}
            max_heap = []
            res = []
            for ch in s:
                if ch in char_count:
                    char_count[ch] += 1
                else:
                    char_count[ch] = 1
            for k,v in char_count.items():
                if v > (len(s)+1)//2:
                    return ''
                max_heap.append([-v,k])
            prev_count,prev_value = 0,''
            heapq.heapify(max_heap)
            while max_heap:
                curr_count,curr_value = heapq.heappop(max_heap)
                res.append(curr_value)
                if prev_count < 0:
                    heapq.heappush(max_heap,[prev_count,prev_value])
                prev_count = curr_count +1
                prev_value = curr_value
            return ''.join(res)


            

            







            

            