class Student:
    name='jobayer'
s1=Student()
print(s1.name)

#contructor
class Student:
    def __init__(self):
        print("adding")
    name='jobayer'
s1=Student()

#method
class Student:
    def welcome(self):
        print("welcome")
    name='jobayer'
s1=Student()
s1.welcome()

#static method
class Student1:
    @staticmethod
    def collage():
        print("collage")
S1=Student1()        
S1.collage()
del S1

#private attribute
class Account:
    def __init__(self,acc_pass):
        self.__acc_pass=acc_pass

A1=Account("123")

#inheritance 
class car:
    def __init__(self,type):
        self.type=type

    def start(self):
        print("start")
class toyota(car):
    
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)


t1=toyota("to","fo")
t1.start() 
print(t1.type)      

#class method
class person:
    name="anonymous"
    @classmethod
    def change(cls,name):
        cls.name=name
p1=person()
p1.change("jobayer")
print(p1.name)
print(person.name)        

#property

class jobayer:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2

    @property
    def percentage(self):
        return str((self.val1+self.val2)/2)+"%"
stu1=jobayer(65,67)
print(stu1.percentage)
stu1.val1=88
print(stu1.percentage)

#polymorphism
#dunder function

class complex :
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"i + ",self.img,"j")    
    def __add__(self,num2):#dunder function
        newReal= self.real+num2.real
        newImg= self.img+num2.img
        return complex(newReal,newImg)  

num1=complex(1,3)
num2=complex(4,5 )
num3=num1+num2
num3.show()     

