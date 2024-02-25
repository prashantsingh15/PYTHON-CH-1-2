n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        #print(j, end="") it is for print 12345 in square box 
        print(n-j+1,end="") #it is for printing in backward direction
        
        j = j + 1
    print()
    i = i + 1