#!/usr/bin/env python
# coding: utf-8

# # Q.1 create a class called rectanglle with attributes such as width and height define methods to calculate the area and perimeter of the rechangle

# In[1]:


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get(self):
        self.area=(self.width*self.height)
        print('Area=',self.area)
        
        self.perimeter=2*(self.width+self.height)
        print('Perimeter=',self.perimeter)


# In[13]:


A=Rectangle(15,35)
A.get()


# # Q.2 create a class called circle with attributes such as redius. define methods to calculate the area and circumference of the circle

# In[3]:


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
        
    def show(self):
        self.area = 3.14 * (self.radius ** 2)
        print('Area',self.area)
        
    
        self.circumference = 2 * 3.14 * self.radius
        print('Circumference',self.circumference)


# In[14]:


B=Circle(10)
B.show()


# # Q.3 create a class called bankaccount with attributes such as balance and interest_rate define methods to deposite , withdraw,and calculate interest on the balance

# In[16]:


class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print('Amount balance shown:',self.balance)
        


# In[18]:


b=BankAccount(10000,0.10)
b.deposit(1000)
b.withdraw(500)
b.calculate_interest()


# # Q.4 create a class called person with  attributes name ,age and gender. include a method called introduce that prints out a message introducing the person with their name age and gender.

# In[7]:


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display_employee_info(self):
        print('Name=',self.name)
        print('Age=',self.age)
        print('Gender=',self.gender)
        
class Employee(Person):
    def __init__(self,name,age,gender,employee_id):
        Person.__init__(self,name,age,gender)
        self.employee_id=employee_id
    def display_employee_info(self):
        Person.display_employee_info(self)
        print('Employee_Id=',self.employee_id)


# In[9]:


e=Employee('tonny',18,'Male',117)
e.display_employee_info()


# # Q.5 create a class called vahicle with attributes make ,model and year include a method called start_engine that print out a message indicing that engine has started.

# In[10]:


class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start_the_engine(self):
        print('Make=',self.make)
        print('Model=',self.model)
        print('Year=',self.year)


# In[19]:


v=Vehicle('ASC','b4u-257',2000)
v.start_the_engine()


# In[ ]:




