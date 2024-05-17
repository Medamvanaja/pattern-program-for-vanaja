for row in range(0,4,1):
  for col in range(0,7,1):
    if((row==col) or(row+col==6)): 
      print("V",end=" ")
    else:
      print(" ",end=" ")
  print()  
  print()
print("--------------------------------------------")
print()
  
  
for i in range(0,6,1):
  for j in range(0,5,1):
    if((j==0 or j==4) and i!=0) or (i==0 or i==3) and (j>0 and j<4):
      print("A",end=" ")
    else:
      print(" ",end=" ")
  print()    
print("--------------------------------------------")
print()
for i in range(0,5):
  for j in range(0,5):
    if((j%4==0)or(i==j)):
      print("N",end=" ")
    else:
      print(" ",end=" ")
  print()
print("--------------------------------------------")
print()
for i in range(0,6,1):
  for j in range(0,5,1):
    if((j==0 or j==4) and i!=0) or (i==0 or i==3) and (j>0 and j<4):
      print("A",end=" ")
    else:
      print(" ",end=" ")
  print()
  
    
print("--------------------------------------------")
print()
for i in range(0,7,1):
  for j in range(0,5,1):
    if j==2 or (i==0 and j!=2)or(i==6 and j<2):
      print("J",end=" ")
    else:
      print(" ",end=" ")
  print()
print("--------------------------------------------")
print()
for i in range(0,6,1):
  for j in range(0,5,1):
    if((j==0 or j==4) and i!=0) or (i==0 or i==3) and (j>0 and j<4):
      print("A",end=" ")
    else:
      print(" ",end=" ")
  print()    
print("--------------------------------------------")
print()

