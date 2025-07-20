class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key_mapp={}
        if len(s)!=len(t):
            return False
        for i in s:
            key_mapp[i] = key_mapp.get(i,0)+1
        for c in t:
            if c not in key_mapp or key_mapp[c] <= 0:
                return False
            key_mapp[c] -= 1
        return True
        

