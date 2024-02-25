# For inverted pattern
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n-i+1:
        print(n-i+1,end ="") # Here we have to know that i is coloumn so we have to minus
        #n-i n is any number from which  we have to minuss from i is called as row we minus 1
        j = j+1
    print()
    i = i+ 1