n = int(input())
q = (n+1)//2 
w = 1
t = 0
for i in range(q):
    for r in range(q-1):
        print(" ",end = "")
    q = q-1
    for s in range(w):
        print("*",end = "")
    w = w+2
    print()

w = 1
h  = (n+1)//2 -1
b = n-2
for i in range(h):
    f = 0
    while (f<w):
        print(" ",end = "")
        f = f+1
    w = w+1
    for r in range(b):
        print("*",end = "")
    b = b-2
    print()