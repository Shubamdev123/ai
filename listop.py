#nested list
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[l1,23,32,l1,12,42]
print(l3)

#length of the list
print(len(l3))

#concatination
a=['a','b','c','d']
b=['e','f','g','h']
print(a+b)

#membership
print('e' in a)
print('a' in a)

#indexing
print(l1[1])

#iteration
for i in l1:
    print(i,end=' ')
print()

#slicing
print(*l1[::2])

#adding elements
f=['apple','mango']
f.insert(1,'banana')
print(f)

#append
f.append('orange')
print(f)

#extend
f.extend(l1)
print(f)

#delete
del f[0]
print(f)