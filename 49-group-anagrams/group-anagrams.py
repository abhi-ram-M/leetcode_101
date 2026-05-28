from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for k in strs:
            a = [0]*26
            for m in k:
                a[ord(m)- ord('a')] += 1
            a = tuple(a)
            if a in dic:
                dic[a].append(k)
            else:
                dic[a] = [k]
        return list(dic.values())





        

        
                

