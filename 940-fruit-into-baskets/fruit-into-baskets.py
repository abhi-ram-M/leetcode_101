class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if 0<n<=10**5:
            max_len = 0
            dic = {}
            l = 0
            r = 0
            while r<n:
                dic[fruits[r]] = dic.get(fruits[r],0)+1
                while len(dic) > 2:
                    dic[fruits[l]] -= 1
                    if dic[fruits[l]] == 0:
                        del dic[fruits[l]]
                    l += 1
                if len(dic)<=2:
                    max_len = max(max_len, r-l+1)
                r+=1
            return max_len
