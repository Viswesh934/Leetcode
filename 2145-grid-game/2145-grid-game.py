class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        fs=sum(grid[0])
        ss=0
        ms=float('inf')

        for i in range(len(grid[0])):
            fs-=grid[0][i]
            ms=min(ms,max(fs,ss))
            
            ss+=grid[1][i]
        return ms




        
        