n =int(input())
i =1
while i<=n:
    j = 1
    start_chr=chr(ord(chr(64+n))+i-1)
    while j<=i:
        charP=chr(ord(start_chr)+j-1)
        print(charP,end='')
        j = j+1
    print()
    i=i+1