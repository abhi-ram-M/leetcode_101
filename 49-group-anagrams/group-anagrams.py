class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mapp = {}
        for k in strs:
            
            s = ''.join(sorted(k))
            if s in mapp:
                mapp[s].append(k)
            else:
                mapp[s] = [k]
        return list(mapp.values())





        

        
                

