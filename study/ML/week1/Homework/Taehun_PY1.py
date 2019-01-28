for i in range(1, 5):			# (5)-1 is nubmer of loop
  k=0
  print(" "*(4-i), end="")		# space
  for j in range(0,i):			# upper shape
    print(k, end='')
    k+=1
  k-=1
  for j in range(0, i-1):
    k-=1
    print(k, end="")  
  print()

for i in range(1,4):			# (4)-1 is number of loop
  k=0
  print(" "*(i), end="")		# space
  for j in range(0,4-i):		# lower shape
    print(k, end='')
    k+=1
  k-=1
  for j in range(0, 3-i):
    k-=1
    print(k, end="")  
  print()




