class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        c=0
        f=0
        s=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
                if c>2:
                    return False
                elif c==1:
                    f=i
                else:
                    s=i
        
        if s1[f]==s2[s] and s1[s]==s2[f]:
            return True
        return False

        