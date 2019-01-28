k = int(input("k :: "))
for x in range(1, k, 2):
    print(" "* ((k - x) // 2),end="")
    for z in range(0, (x-1)//2 , 1):
        print(z,end="")
    for j in range((x-1)//2, -1, -1):
        print(j,end="")
    print()
for y in range(k, 0, -2): #
    print(" " * ((k - y) // 2),end="")
    for i in range(0, (y-1)//2, 1):
        print(i,end="")
    for l in range((y-1)//2, -1, -1):
        print(l,end="")
    print()
