n = int(input("Enter a number: "))          #우선 n번째 소수를 찾기 위해 n을 입력받음
cnt = 0                                     #cnt=0, i=1로 초기화함(cnt는 지금까지 소수의 개수를 나타내고, i는 1씩 증가하며 특정한 수가 소수인지 아닌지 판별함)
i = 1

while cnt<n:                        #n번째 소수를 찾을 때까지
    check = 0                       #특정한 수가 소수인지 아닌지 판단하기 위해 check 변수 사용

    i = i + 1
    for j in range(2, i):           #2부터 i-1까지 돌며
        if i%j==0:                  #그 수들 중 i가 적어도 하나로 나누어 떨어지면 check를 1로 바꿔 i가 소수가 아님을 나타냄
            check = 1
            break

    if check==0:                    #check가 0이라는 것은 i가 소수라는 것이므로
        cnt = cnt + 1               #소수 하나를 더 찾았으니 cnt 값을 1 증가시킴

print("The number you're looking for is %d" %i)         #n번째 소수 출력!
    
        
    
