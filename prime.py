n=int(input("enter the prime number"))
c=0
num=2
while c<n:
    p=True
    for i in range(2,num):
        if num%i==0:
            p=False
            break
    if p:
        print(num,end=' ')
        c+=1
    num+=1
print()
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if c==2:
    print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")
