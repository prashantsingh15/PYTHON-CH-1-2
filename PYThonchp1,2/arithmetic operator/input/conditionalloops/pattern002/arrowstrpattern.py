width = int(input("Enter the width of arrow: ")) 
for i in range(1, width+1): 
    for j in range(1, (width-i)+1): 
        print(" ", end="") 
    for k in range((width-i)+1): 
        print("*", end="") 
    print() 
for i in range(1, width): 
    for j in range(1,i+1): 
        print(" ", end="") 
    for k in range(1, (i+1)+1): 
        print("*", end ="") 
    print()