n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=i:
        print(j,end='')
        j = j+1
    spaces = 1
    while spaces<=2*(n-i):
        print(' ', end ='')
        spaces = spaces +1

    p = i
    j = 1
    while j<=i:
        print(p,end= '')
        p = p-1
        j = j+ 1
    print()
    i = i+1

