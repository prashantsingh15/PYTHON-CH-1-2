# Count number 
n  = int(input())
count = 0

while n != 0:
    n //= 10
    count += 1

print("Number of digits: "+str(count))
