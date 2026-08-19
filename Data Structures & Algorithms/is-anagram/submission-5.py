class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp={}        
        for i in range(len(s)):
            temp[s[i]]=temp.get(s[i],0)+1
            temp[t[i]]=temp.get(t[i],0)-1
        bool=True
        for i in temp.values():
            if i!=0:
                bool =False
        return bool