class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store=set(nums)
        res=0
        for num in nums:
            cur,streak=num,0
            while cur in store:
                cur=cur+1
                streak+=1
            res=max(res,streak)
        return res