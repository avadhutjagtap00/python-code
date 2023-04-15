#!/usr/bin/env python
# coding: utf-8

# # Q. 1. Write a program to print yourself introduction.

# In[16]:


name=input('Enter your name :- ')
email_id=input('Enter your email:- ')
Mobile_number=input('Enter your mobile number :- ')
Qualification = input('Enter your highest qualification :- ')
Work_experience = input('Enter your experience in year :- ')
Date_of_birth =input('Enter your date of birth :- ')
Gender=input('Enter your gender:- ')
Language_known=input('Enter language you known:- ')
Hobbies=input('Enter your Hobbies:- ')


# In[4]:


introduction = ("Hello, my name is avadhut jagtap i am from maharashtra i have graduate in b.com it i am pursing m.b.a second year from Dy patil university in pune i am a fresher thats all about me thank you")
print(introduction)


# # Q 2. Write a program to perform the following operations: Addition, Subtraction, Multiplication, Division, Modulus, Exponent.

# In[5]:


## Addition
a = int(input('Enter the number :'))
b = int(input('Enter the number :'))

add = a+b

print('Addition=',add)


# In[6]:


## Subtraction
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

sub = a-b

print('Subtraction=',sub)


# In[7]:


## Multiplication
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

mul = a*b

print('Multiplication=',mul)


# In[9]:


## Division
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

div = a/b

print('Division=',div)


# In[10]:


## Modulus
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

mod = a%b

print('Modulus=',mod)


# In[11]:


## Exponent
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

exp = a**b

print('Exponent=',exp)


# # Q 3. Write a program to swap two numbers.

# In[12]:


a=int(input('Enter the number :- '))
b=int(input('Enter the number :- '))

print('The value of a before swap:- ',a)
print('The value of b before swap:- ',b)

temp=a
a=b
b=temp

print('The value of a after swap:- ',a)
print('The value of b after swap:- ',b)


# ## Q 4. Write a program to swap two numbers w/o using 3rd variable.¶

# In[2]:


a=int(input('Enter the number :- '))
b=int(input('Enter the number :- '))

print('The value of a before swap:- ',a)
print('The value of b before swap:- ',b)

a,b=b,a

print('The value of a after swap:- ',a)
print('The value of b after swap:- ',b)


# # Q 5. Write a program to compute simple interest.¶

# In[3]:


p = int(input('Enter the principal amount:- '))
r = int(input('Enter the rate of interest:- '))
t = int(input('Enter the time:- '))

Simple_Interest=(p*r*t)/100

print('Simple intrest is:- ',Simple_Interest)


# # Q 6. Write a program to find average of 5 numbers by user input.

# In[4]:


num1=int(input('Enter the number :- '))
num2=int(input('Enter the number :- '))
num3=int(input('Enter the number :- '))
num4=int(input('Enter the number :- '))
num5=int(input('Enter the number :- '))

ave = (num1+num2+num3+num4+num5)/5

print('Average of given numbers is:- ',ave)


# # Q 7. Write a program to calculate the discriminant of the quadratic equation.

# In[5]:


a = float(input('Enter the value of a :- '))
b = float(input('Enter the value of b :- '))
c = float(input('Enter the value of c :- '))

dis = (b**2) - (4*a*c)

print('The discriminant of the quadratic equation is',dis)


# # Q 8. Write a program to calculate the areas of Rectangle, Square, Triangle and Circle.¶

# In[7]:


# area of Rectangle

length = int(input('Enter the length of rectangle:- '))
Width = int(input('Enter the width of rectangle:- '))

area = length * Width

print('Area of rectangle is:- ',area)


# In[8]:


# area of Square

side = int(input('Enter the side of square:- '))

area = side * side

print('Area of square is:- ',area)


# In[9]:


# area of Triangle

base = int(input('Enter the base of triangle:- '))
height = int(input('Enter the height of triangle:- '))

area = (base*height)/2

print('Area of triangle is:- ',area)


# In[10]:


# area of Triangle

base = int(input('Enter the base of triangle:- '))
height = int(input('Enter the height of triangle:- '))

area = (base*height)/2

print('Area of triangle is:- ',area)


# # Q 9. Write a program to calculate net salary of an employee whose basic salary is entered by user, DA is 5% of basic salary, HRA is 7% of basic salary and PF is 3% of basic salary.¶

# In[11]:


basic_salary = float(input('Enter the basic salary:- '))
DA = .05*basic_salary
HRA = .07*basic_salary
PF = .03*basic_salary

net_salary = (basic_salary+DA+HRA)-PF

print('DA :- ',DA)
print('HRA :- ',HRA)
print('PF :- ',PF)

print('Net salary is:-',net_salary)


# # Q 10. Write a program to calculate power of number.

# In[12]:


base = int(input('Enter the base:- '))
exponent = int(input('Enter the exponent:- '))

power = base**exponent

print('The power of number is :- ',power)
# 


# # Q 11. Write a program to get the python version you are using.

# In[13]:


from platform import python_version


# In[14]:


python_version()


# In[15]:



import sys 
print("Python version") 
print (sys. version) 
print("Version info.") 
print (sys. version_info)
from platform import python_version 
print(python_version())


# In[ ]:




