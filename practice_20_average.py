class student :
    def __init__(self,phy,math,che):
        self.phy = phy
        self.math = math
        self.che = che
    def average(self):
        av=(self.phy+self.che+self.math)/3
        return av
s1=student(10,20,30)
av1=s1.average()  
print(av1)  

class Account :
    balance=100
    account_no=123
    def debit(self):
        pass
    def credit(self):
          
        print(self.balance)  

A1=Account()
A1.credit()

class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print(3.14*self.r*self.r)

    def perimeter(self):
        print(2*3.14*self.r)

r1=circle(3)
r1.area()
r1.perimeter()   

class employee:
    role="manager"
    department="account"
    salary=90000

class engineer(employee):
    name="jobayer"
    age=22

q1=engineer()
print(q1.salary)        

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False    
or1=order("pen",5)
or2=order("book",10)
print(or1>or2)        