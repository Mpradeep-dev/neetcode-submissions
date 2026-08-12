from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        cnt=Counter(nums)
        s=sorted(cnt.items(),key=lambda x :x[1],reverse=True)
        ans=[n for n,m in s]
        return ans[:k] 