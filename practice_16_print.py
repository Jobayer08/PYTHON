i=1
while i<=100:
    print(i)
    i+=1

i=100
while i>=1:
    print(i) 
    i-=1

n=int(input("enter number "))
i=1
while  i<=10:
    print(n,"* ",i,"= ",n*i)
    i+=1  
i=1
c=3
while i<=100:
    print(i)
    i=i+c
    c+=2    
num=(1,4,9,16,25,36,49,64,81,100)   
i=0

while i<len(num):
    if n==num[i]:
     print("found")
     break
    i+=1 
if i==10:
    print("not found")

num=[1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)

num=(1,4,9,16,25,36,49,64,81,100)
for i in num:
    if i==n:
        print("found",n)
        break
    print(i)    

for j in range(1,101):
    print (j) 
for j in range(100,0,-1):
    print (j)      
for j in range(1,11):
    print(j*n)    
i=1
j=0
while i<=n:
    j=j+i
    i+=1
print(j) 
k=1    
for j in range(1,n+1):
    k=k*j
print(k)        
