n = int(input())
i = 1
while i<=n:
    j = 1
    
    start_chr =chr(ord('A') + i-1)
    while j<=i:
        chrP=chr(ord(start_chr) +j-1)
        print(chrP,end='')
        j = j + 1
        
        
    print()
    i = i + 1
