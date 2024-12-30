list1=[1,2,3]
def pri(li):
    print(len(li))
pri(list1)

def pri1(li):
    for i in li:
     print(i,end=' ')
pri1(list1)     

def fact(n):
   k=1
   for i in range(1,n+1):
      k=k*i
   print(k)
fact(5)