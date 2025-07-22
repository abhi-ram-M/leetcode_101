class Solution:
    def reorganizeString(self, s: str) -> str:
        if (1 <= len(s) <= 500):
            import heapq
            char_count = {}
            res = []
            for char in s:
                char_count[char] = char_count.get(char,0)+1
            max_heap = []
            for char,count in char_count.items():
                if count > (len(s)+1)//2:
                    return ''
                max_heap.append((-count,char))
            heapq.heapify(max_heap)
            prev_count = 0
            prev_char = ''
            while max_heap:
                count,char = heapq.heappop(max_heap)
                res.append(char)
                if prev_count < 0:
                    heapq.heappush(max_heap,(prev_count,prev_char))
                prev_count= count+1
                prev_char =char
            return ''.join(res)

            







            

            