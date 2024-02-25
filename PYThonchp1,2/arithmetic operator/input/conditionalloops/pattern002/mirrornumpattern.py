n =int(input())
i =  1
while i<=n:
    spaces = 1
    while spaces <= n-i:
        print(' ',end="")
        spaces = spaces+1
    num = 1
    while num<=i:
        print(n-i,end="")
        num = num +1
    print()
    i = i +1