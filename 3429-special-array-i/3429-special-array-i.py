class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        t=True
        for i in range(1,len(nums)):
            if ((nums[i-1]&1)^(nums[i]&1))==0:
                return False
            
        return True
        