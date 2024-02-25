k = int(input())
i = 1
while i<=k:
    j = 1
    p = i
    start_chr =chr(ord('A') + i - 1)
    while j<=i:
        chrP=chr(ord(start_chr) + j - 1)
        print((chrP),end='')
        j = j + 1
        p = p + 1
    print()
    i = i + 1
