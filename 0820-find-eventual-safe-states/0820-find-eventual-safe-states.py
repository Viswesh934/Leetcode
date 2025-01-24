from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)

        adj=[[] for _ in range(n)]

        outdegree=[0]*n

        for i in range(len(graph)):
            for node in graph[i]:
                adj[node].append(i)
                outdegree[i]+=1
        q=deque()
        for i in range(n):
            if outdegree[i]==0:
                q.append(i)
        safe=[False]*n
        while q:
            node=q.popleft()
            safe[node]=True
            for i in adj[node]:
                outdegree[i]-=1
                if outdegree[i]==0:
                    q.append(i)
        safes=[]

        for i in range(n):
            if safe[i]:
                safes.append(i)
        return safes

                



        q=deque()


        


        