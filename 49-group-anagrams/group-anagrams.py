from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for k in strs:
            s = ''.join(sorted(k))
            if s in dic:
                dic[s].append(k)
            else:
                dic[s] = [k]
        return list(dic.values())





        

        
                

