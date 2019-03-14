n = int(input("Enter a number: "))
cnt = 0
i = 1

while cnt<n:
    check = 0

    i = i + 1
    for j in range(2, i):
        if i%j==0:
            check = 1
            break

    if check==0:
        cnt = cnt + 1

print("The number you're looking for is %d" %i)
    
        
    
