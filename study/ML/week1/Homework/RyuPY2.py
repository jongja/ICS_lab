for i in range(0, 7):
    if i < 4:
        arr = " "*(3-i)
        for j in range(0,i+1):
            arr +=str(j)
        reverse = arr[::-1]
        arr += reverse[1:]
        print(arr)

    elif i>=4:
        arr = " "*(i-3)
        for j in range(0,7-i):
            arr +=str(j)
        reverse = arr[::-1]
        arr += reverse[1:]
        print(arr)
