class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        fi=strs[0]
        sec=strs[-1]
        ans=""
        for i in range(min(len(fi),len(sec))):
            if fi[i]==sec[i]:
                ans+=fi[i]
            else:
                break
        return ans