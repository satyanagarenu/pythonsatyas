def twinprime(n):
  list1=[]
  for i in range(1,n+1):
    count=0
    for j in range(2,n+1):
      if i%j==0:
          count=count+1
    if count==1:
      list1.append(i)
    count=0
  print(list1) 
  for i in list1:
    if i in list1 and i+2 in list1:
      print(i,i+2)
twinprime(1000)
    
