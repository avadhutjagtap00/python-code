#!/usr/bin/env python
# coding: utf-8

# # Q 1. Write a program to check whether a given number is even or odd.

# In[ ]:


num = int(input("enter your nunmer"))
if num % 2 == 0:
    print("this no. is even")
else:
    print("this no. is odd")


# # Q 2. Write a program to check whether an alphabet is a vowel or consonant.¶

# In[5]:


vowel =('A','E','I','O','U','a','e','i','o','u')

alp = input('Enter the alphabet:-')

if alp in vowel:
    
    print('THIS IS VOWEL THANK YOU:-',alp)
    
else:
    print(' THIS IS NOT SORRY:-',alp)


# # Q 3. Write a program to check whether a person is eligible to vote or not

# In[4]:


age = int(input('Enter your age:-'))
if age >= 18:
    print('You are eligible for voting ')
    
else:
    print('You are not eligible for voting')
    
print('thank you')


# # Q 4. Write a program to check whether a given number is positive, negative or zero.¶

# In[5]:


num = int(input('Enter the number:- '))

if num > 0:
    print('Number is positive ')
    
elif num == 0:
    print('Number is zero')
    
else:
    print('Number is negative ')


# # Q 5. Write a program to check whether a given year is leap year or not.

# In[7]:


year = int(input('Enter the year'))

if (year % 400 == 0) or (year % 4 ==0) and (year % 100 != 0):
    print('Leap year')
    
else:
    print('Not a leap year')


# # Q 6. Write a program to check a triangle is equilateral, isosceles or scalene.

# In[8]:


side1 = int(input('The value of side1:- '))
side2 = int(input('The value of side2:- '))
side3 = int(input('The value of side3:- '))

if side1 == side2 == side3:
    print('Triangle is equilateral')
    
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('Triangle is isosceles')
    
else:
    print('Triangle is scalene')


# # Q 7. Write a program to check whether after selling a product its profit or loss.¶

# In[4]:


actual_cost = float(input(" Please Enter the Actual Product Price: ")) 
sailing_cost = float(input(" Please Enter the Sales Amount: ")) 

amount = sailing_cost - actual_cost

if(sailing_cost - actual_cost > 0): 
    print("Great it's profit. Total profit  Amount = ",amount)
    
elif (sailing_cost - actual_cost < 0):
    print("it's loss. Total loss  Amount = ",abs(amount))
    
else:
    print('No profit no loss')


# # Q 8. Write a program to enter two numbers and print the greatest number.

# In[2]:


num1 = int(input('Enter the number:- '))
num2 = int(input('Enter the number:- '))

if num1 > num2:
    print('num1 is greatest')
    
elif num2 > num1:
    print('num2 is greatest')
    
else:
    print('two number are same')


# # Q 9. Write a program to enter two numbers and print the smallest number.

# In[3]:


num1 = int(input('Enter the number:- '))
num2 = int(input('Enter the number:- '))

if num1 < num2:
    print('num1 is smallest')
else:
    print('num2 is smallest')


# # Q 10. Write a program to enter three numbers and print the greatest number.

# In[7]:


num1 = int(input('Enter the number:- '))
num2 = int(input('Enter the number:- '))
num3 = int(input('Enter the number:- '))

if num1 > num2 and num1 > num3:
    print('Num1 is greatest number')
    
elif num2 > num1 and num2 > num3:
    print('Num2 is greatest number')
    
elif num3 > num1 and num3 > num2:
    print('Num3 is greatest number')
    
else:
    print('all numbers are equal')


# # Q 11. Write a program to enter three numbers and print the smallest number

# In[9]:


num1 = int(input('Enter the number:- '))
num2 = int(input('Enter the number:- '))
num3 = int(input('Enter the number:- '))

if num1 < num2 and num1 < num3:
    print('Num1 is smallest number')
    
elif num2 < num1 and num2 < num3:
    print('Num2 is smallest number')
    
elif num3 < num1 and num3 < num2:
    print('Num3 is smallest number')
    
else:
    print('all numbers are equal')


# # Q 12. Write a program to calculate the roots of quadratic equation.

# In[10]:


# Python program to find roots of quadratic equation
a = int(input())
b = int(input())
c = int(input())

import math


# function for finding roots
def equationroots( a, b, c):

# calculating discriminant using formula
dis = b * b - 4 * a * c
sqrt_val = math.sqrt(abs(dis))

# checking condition for discriminant
if dis > 0:
    print(" real and different roots ")
    print((-b + sqrt_val)/(2 * a))
    print((-b - sqrt_val)/(2 * a))

elif dis == 0:
    print(" real and same roots")
    print(-b / (2 * a))
# when discriminant is less than 0
else:
    print("Complex Roots")
    print(- b / (2 * a), " + i", sqrt_val)
    print(- b / (2 * a), " - i", sqrt_val)



# # Q 13. Write a program to enter a number between (1 – 7) and print the respective day of the week.

# In[16]:


num=int(input('Enter the number:- '))
if num==1:
    print("It's Monday")
elif num==2:
    print("It's Tuesday")
elif num==3:
    print("It's Wednesday")
elif num==4:
    print("It's Thursday")
elif num==5:
    print("It's Friday")
elif num==6:
    print("It's Saturday")
elif num==7:
    print("It's Sunday")
else:
    print('check the number')


# # Q 14. Write a program to enter a number between (1 – 12) and print the respective months.¶

# In[17]:


num = int(input('Enter the number:- '))

if (num==1):
    print ("It's Jan")
    
elif (num==2):
    print("It's Feb")
    
elif (num==3):
    print("It's March")
    
elif (num==4):
    print("It's April")
    
elif (num==5):
    print("It's May")
    
elif (num==6):
    print("It's June")
    
elif (num==7):
    print("It's July")
    
elif (num==8):
    print("It's August")
    
elif(num==9):
    print("It's September")
    
elif(num==10):
    print("It's October")
    
elif(num==11):
    print("It's November")
    
elif(num==12):
    print("It's December")
    
else:
    print('Invalid input')


# In[25]:


import calendar

num = int(input('Enter the month number:- '))

print(" It's ", calendar.month_name[num])


# # Q 15. Write a program to enter a number between (1 – 4) and perform the following functions.¶

# In[28]:


num = int(input('Enter the number which function you want to perform :- '))
a = int(input('value of a:- '))
b = int(input('value of b:- '))

if num == 1:
    add = a + b
    print('addition is =',add)
    
elif num == 2:
    sub = a - b
    print('subtraction is =',sub)
    
elif num == 3:
    mul = a * b 
    print('multiplication is =',mul)
    
elif num == 4:
    div = a / b
    
    print('division is =',div)
    
else:
    print('Please check the number')


# # Q 16. Write a program to convert Temperature from Celsius to Fahrenheit.¶

# In[ ]:


temp = float(input('Enter the temperature:- '))
unit = input('Enter the unit of temperature:- ')
if unit == "C" or unit == "c":
    far = (temp * 1.8) + 32
    print(f'Temperature in fahrenheit is {far} F')
elif unit == "F" or unit == "f":
    cel = (temp - 32) / 1.8
    print(f'Temperature in fahrenheit is {cel} C')
else:
    print('please check the entered details')


# # Q 17. A company decides to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# In[ ]:


year_of_service = float(input('Enter your year of service:- '))
salary = float(input('Enter your salary :- '))

if year_of_service >= 5:
    bonus = salary * 0.05
    print('Congratulations you got bonus of ',bonus)
    
else:
    print('Sorry you are not eligible for bonus')


# # Q 18. Write a program to take input of length and breadth of a rectangle from user and check if it is square or not.¶
# 

# In[ ]:


length = int(input('Enter the value of length:- '))
breadth = int(input('Enter the valur of breadth:- '))

if length == breadth:
    print("Rectangle is square")
else:
     print("Rectangle is not square")


# # Q 19. Take input of age of 3 people from user and determine oldest and youngest among them.

# In[ ]:


print('Person person1 = int(input("Enter age Person 1: "))
person2 = int(input("Enter age Person 2: "))
person3 = int(input("Enter age Person 3: "))

if (person1 > person2) & (person1 > person3):
    print('Person 1 is the oldest')
    if person2 < person3:
   print('Person 2 is the youngest')
    else:
   print('Person 3 is the youngest')
elif (person2 > person1) & (person2 > person3):
    print('Person 2 is the oldest')
    if person1 < person3:
   print('Person 1 is the youngest')
    else:
   print('Person 3 is the youngest')
else:
    print('Person 3 is the oldest')
    if person1 < person2:
   print('Person 1 is the youngest')
    else:2 is the youngest


# # Q 20. A school has following rules for grading system: a. Below 25 – F b. 25 to 45 – E c. 45 to 50 – D d. 50 to 60 – C e. 60 to 80 – B f. Above 80 – A Ask user to enter their marks and print corresponding grades.

# In[1]:


marks = int(input('Enter your marks:- '))
if marks >= 80 and marks <= 100:
    print('excellent  you got A grade')
elif marks >= 60 and marks < 80:
    print('very Good you got B grade')
elif marks >= 50 and marks < 60:
    print('Good you got C grade')
elif marks >= 45 and marks < 50:
    print('you got D grade')
elif marks >= 25 and marks < 45:
    print('You got E grade')
elif marks < 25:
    print('Your fail')
else:
    print('please check entered marks')
    


# In[ ]:




