class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        def mul(s,nums):
            sum=1
            for i in range(len(nums)):
                
                if i==s:
                    continue
                else:
                    sum*=nums[i]
                    
            return sum
        for i in range(len(nums)):
            ans.append(mul(i,nums))
        return ans