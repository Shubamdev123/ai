import math
def ab(cur,ni,mt,s,t,a,b):
    if cur==t:
        return s[ni]
    if mt:
        max1=-math.inf
        l=ab(cur+1,ni*2,False,s,t,a,b)
        max1=max(max1,l)
        a=max(a,max1)
        if b<=a:
            return max1
        r=ab(cur+1,ni*2+1,False,s,t,a,b)
        max1=max(max1,r)
        return max1
    else:
        min1=math.inf
        l=ab(cur+1,ni*2,True,s,t,a,b)
        min1=min(min1,l)
        b=min(b,min1)
        if b<=a:
            return min1
        r=ab(cur+1,ni*2+1,True,s,t,a,b)
        min1=min(min1,r)
        return min1

n=int(input("Enter value: "))
s=list(map(int,input().split()))
t=math.log(len(s),2)
print("optimal value is:",end="")
print(ab(0,0,True,s,t,-math.inf,math.inf))