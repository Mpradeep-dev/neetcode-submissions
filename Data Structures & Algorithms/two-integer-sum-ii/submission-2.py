class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=[]
        for i in range(len(numbers)):
            sec_value=target-numbers[i]
            if numbers[i] in seen:
                return [numbers.index(sec_value)+1,i+1]
            else:
                seen.append(sec_value)