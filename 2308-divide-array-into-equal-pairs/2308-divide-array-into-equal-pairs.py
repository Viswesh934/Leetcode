class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)
        d={}
        if n%2!=0:
            return False
        v=n//2
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]%2!=0:
                return False
        return True
        