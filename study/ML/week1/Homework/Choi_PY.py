print('보고싶은 크기를 입력하시오',end="")
temp = int(input())
for i in range(temp + 1):
    for j in range(temp - i):
        print(' ',end="")
    for j in range(i + 1):
        print(j,end="")
    for j in range(i,0,-1):
        print(j-1,end="")
    print('')
for i in range(temp):
    for j in range(i + 1):
        print(' ',end="")
    for j in range(temp - i):
        print(j, end="")
    for j in range(temp - i -1,0,-1):
        print(j-1,end="")
    print('')
