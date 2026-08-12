class Solution:
    def isValid(self, s: str) -> bool:
        v=""
        while s!=v:
            v=s
            s=s.replace("[]","").replace('{}','').replace('()','')
        return s==""