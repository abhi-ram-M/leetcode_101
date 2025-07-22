class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l<r:
            while l<r and not self.alp(s[l]):
                l += 1
            while l<r and not self.alp(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    


    def alp(self,c):
        return ('A'<=c<='Z') or ('0'<=c<='9') or ('a'<=c<='z')

