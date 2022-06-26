i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer than less than 6")

a=[1,2,3,4]
while a:
    print(a.pop())

count=0
while (count<5):count +=1; print("Hello Aisha")

i=0
a='geeksforgeeks'
while i<len(a):
    if a[i]=='g' or a[i]=='s':
        i+=1
        continue
    print('Current Letter:', a[i])
    i+=1