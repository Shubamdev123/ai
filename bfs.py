def bfs(g,s):
    v=[]
    q=[s]
    while q:
        n=q.pop(0)
        if n not in v:
            v.append(n)
            q.extend(g[n])
    return v

n=int(input())
g={}
for i in range(n):
    ne=list(map(int,input("enter the numbers of each vertices").split()))
    g[i]=ne

s=int(input("enter the starting vertex"))
res=bfs(g,s)
print("bfs is ",res)