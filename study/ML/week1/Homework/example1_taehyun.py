#for x in range(1, 7, 2):
    #print((" " * ((7 * 2 - 1 - x) // 2)) + ("i" * x))
#for y in range(7, 0, -2):
#    print((" " * ((7 * 2 - 1 - y) // 2)) + "i" * y)

for x in range(0, 6, 2):
    if x == 0:
        print(" " * (6-x // 2), end = "")
        print("0")
    if x == 2:
        print(" " * (6 - x // 2), end = "")
        print("010")
    if x == 4:
        print(" " * (6 - x // 2), end = "")
        print("01210")
for y in range(6,-2,-2):
    if y == 6:
        print(" " * (6 - y // 2), end = "")
        print("0123210")
    if y == 4:
        print(" " * (6 - y // 2), end = "")
        print("01210")
    if y == 2:
        print(" " * (6 - y // 2), end = "")
        print("010")
    if y == 0:
        print(" " * (6 - y // 2), end = "")
        print("0")
