n = int(input())
i = 1
while i <= n:
    spaces = 1
    # spaces
    while spaces <= n - i:
        print(' ', end='')
        spaces = spaces + 1
    p = 1
    j = 1
    # increasing seq
    while j <= i:
        print(p, end='')
        j = j + 1
        p = p + 1
    # decreasing seq
    p = i - 1
    while p >= 1:
        print(p, end='')
        p = p -1
    print()
    i = i + 1




