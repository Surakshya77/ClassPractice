#Topics
# elif
# nested if...else
# function
# oop
# constructor
# import library(example calender)

#1...elif-->if you have more than 2 options

#eg:
num=-5
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is Negative")
else:
    print("Number is Zero")


#2.Nested else if-->if..else statement inside another if..else statement

#eg:
# num=float(input("Enter a number:"))
# if num>=0:
#     if num==0:
#         print("The number is 0")
#     else:
#         print("The number is positive")
# else:
#     print("The number is negative")

#3.Function-->a block of code which runs after it is called
#def fun_name(parameter)
#def abc(username,password)

def abc(name):
    print("Hello",name)
abc("Surakshya")
abc("Kesari")
abc("Nikita")

def add(num1,num2):
    return (num1 + num2)
print(add(2,7))


x=10
def fun():
    x=5
    print("Value of x inside the function:",x)
fun()
print("Value of x outside the function",x)


#6. oop-->object oriented programming language
#class--> collection of data and function sets
#object--> instance of class

#Example:
class myClass:
    a=100
    def fun1(self):
        print("Hello")
obj = myClass()
print(obj.a)
obj.fun1()

#Example2:
class calculator:
    def add(self,num1,num2):
        return num1 + num2
    def mul(self,num1,num2):
        return num1 * num2

calc = calculator()
print(calc.add(3,4))
print(calc.mul(2,4))


#7.Constructor--> It is a class function with double underscore
#__init__(), function is being called when object is created

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def print_emp_details(self):
        print("Employee Name :",self.name)
        print("Employee Id:",self.id)

emp1 = Employee("Surakshya",1)
emp2 = Employee("Hari",2)
emp3 = Employee("Gita",3)
emp4 = Employee("Shyam",4)
emp1.print_emp_details()
emp2.print_emp_details()
emp3.print_emp_details()
emp4.print_emp_details()

#8. import library(example calender)
import calendar
yy=2024
mm=7
dd=8
print(calendar.month(yy,mm,dd))