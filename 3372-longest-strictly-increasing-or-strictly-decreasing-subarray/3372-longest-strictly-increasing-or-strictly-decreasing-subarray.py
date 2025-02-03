class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c=1
        d=1
        r=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                c+=1
                d=1
            elif nums[i-1]>nums[i]:
                d+=1
                c=1
            else:
                d=1
                c=1
            r=max(r,c,d)
        return r

        