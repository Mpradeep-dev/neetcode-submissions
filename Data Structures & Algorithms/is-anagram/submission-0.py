class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            s=sorted(s)
            t=sorted(t)
            for j,i in zip(s,t):
                if j==i:
                    continue
                else:
                    return False
                    break
            return True