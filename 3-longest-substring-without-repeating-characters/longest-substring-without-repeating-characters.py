class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        char_set = set()
        count = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                count -=1
            char_set.add(s[r])
            count +=1
            res = max(res,count)
        return res
            
                

            
                
        