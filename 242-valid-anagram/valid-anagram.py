class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapp = {}
        for a in s:
            mapp[a] = mapp.get(a,0)+1
        for k in t:
            if k not in mapp:
                return False
            mapp[k] = mapp[k]-1
            if mapp[k] < 0:
                return False
        return True


