class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key_mapp={}
        key_mapp2 ={}
        if len(s)!=len(t):
            return False
        for i in s:
            key_mapp[i] = key_mapp.get(i,0)+1
        for c in t:
            key_mapp2[c]=key_mapp2.get(c,0)+1

        if key_mapp2 == key_mapp:
            return True
        else :
            return False
        

