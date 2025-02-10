class Solution:
    def clearDigits(self, s: str) -> str:
        r=[]
        for i in range(len(s)):
            if r and s[i].isdigit():
                r.pop()
            else:
                r.append(s[i])
        print(r)
        return ''.join(r)


                
        