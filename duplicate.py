a=list(map(str,input().split(' ')))
u=[]
for i in a:
    if i not in u:
        u.append(i)
print("after removed duplicate values are:",*u)