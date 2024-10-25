def dfs(g,s):
    v=[]
    st=[s]
    while st:
        no=st.pop()
        if no not in v:
            v.append(no)
            st.extend(reversed(g[no]))
    return v

n=int(input())
g={}
for i in range(n):
    ne=list(map(int,input("enter the no. ").split()))
    g[i]=ne

s=int(input("enter the starting vertex"))
res=dfs(g,s)
print(res)