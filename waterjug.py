def waterj(j1,j2,target):
    jug1,jug2=0,0
    s=[(jug1,jug2)]
    while(jug1!=target and jug2!=target):
        if jug1==0:
            jug1=j1
        elif jug2==j2:
            jug2=0
        else:
            transfer=min((jug1,j2-jug2))
            jug1-=transfer
            jug2+=transfer
        s.append((jug1,jug2))
        if(jug1==target or jug2==target):
            break
    return s

j1=int(input("enter the capacity of jug1: "))
j2=int(input("enter the capacity of the jug2: "))
target=int(input("enter the target: "))
s=waterj(j1,j2,target)
for jug1,jug2 in s:
    print(f"Jug1 :{jug1}  Jug2: {jug2}")
