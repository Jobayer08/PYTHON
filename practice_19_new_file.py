f=open("practice.txt", "w")
f.write("Hi everyone\nwe are learning file io \nusing java.\ni like programming in java")
f.close()
with open("practice.txt", "r") as f:
    data=f.read()
    data=data.replace("java","python")
with open("practice.txt", "w") as f:
    f.write(data)    
with open('practice.txt', 'r') as file:
        content = file.read()
        if 'learning' in content:
            print('string exist')
        else:
            print('string does not exist') 
c=0             
with open('practice.txt', 'r') as f:
     lines=f.readlines()
     for row in lines:
          if row.find('learnig') != -1:
               print('string exist\n',lines.index(row))
               c=1
if c==0 :
     print(-1)       

with open('practice1.txt', 'w+') as f:
     f.write("1,2,4,44,67,89,100,")
     f.seek(0)
     data=f.read()
     print(data)
     num=""
     c=0
     for i in range(len(data)):
          if(data[i]==','):
               print(int(num))
               if(int(num) % 2==0):
                    c+=1
               num=''
          else:
               num+=data[i]     
print(c)