##variables##
"""
user_age=30  #defifing a variable using underscore
userName="raunak" #defining a variable using camel case 
print(userName)
"""

##operators##
#aritmetic operators
"""
num1=10
num2=5

add=print(num1+num2) # +
sub=print(num1-num2) # -
multi =print(num1*num2)  #*
div=print(num1/num2) # /
mod=print(num1 % num2 ) # %
expon=print(num1 ** num2) #**

##comparison operator
greater_than=print(num2>num1) # >
less_than=print(num1<num2) # <
equal_to= print(num2==num1) # ==
not_equal=print(num2 != num1) # !=
greater_than_equal_to=print(num2 >=num1) # >=
less_than_equal_to=print(num1<=num2) #<=

#logical operators (and , or not)
is_true=True
is_false=False 

logical_and=print(is_true and is_false) 
logical_or=print(is_true or is_false) 
logical_not=print(not is_true )

#assignment operator 
x=5
y=10

x+=y #x=x+y
print(x)
y-=x #y=y-x
print(y)

"""

#data types 
""""
#1integer-whole no without a decimal point 
user_age=30
mobile_no=9426470174

# 2. floats-number with a decimal point
user_height=1.82

# 3. string-textual data enclosed in double of single quotes 
user_name="raunak abhani"
user_agee="30"  #no can also be added as string is used inside a double or single quotes

"""
"""
#type casting -basically used for converting one data type into another 
# a) converting to integer 
x=int(4.323422)
y=int('4')
#but it wont convert "hello" or "4.3213" to an integer

# b) converting to float
a=float("2.016")
b=float(2)

#c) converting to string 
#converting a no to a string 
s=str(2.1)

#data structure

#list 
number=[1,2,3,4,5]

#slice
number_slice=number[1:4]

#tuple
person=('john',25,'USA')

#dictionary
person_dict={'name':'john','age':25,'country':'USA'}


#input and print in python

#1. acepting an integer input
x=int(input())
print(x)

# 2. accepting a float input 
y=float(input())

# 3. accepting  string input 
z=str(input())

#print
print("welcome to raspberry pi for begineer course ")

"""


"""
#if loop
x=5
if x>0:
    print("x is positive")
elif x==0:
    print("x is zero")
else:
    ("x is negative")

#while loop

count=0
while count<5:
    print("count:",count)
    count+=1 #count=count+1

#for loop

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

for number in range(1,6):
    print(number)



"""
"""
#break and continue 

fruits=["apple","banana","cherry"]
for fruit in fruits:
    if fruit=="cherry":
        break
    print(fruit)

"""
"""
#try and except 

try:
    x=10/0
except ZeroDivisionError:
    print("error:division by zero is not allowed ")

"""    

#funtions in python

# first define the fuction
def greet(name):
    print('hello,'+name+"!")

#calling that function
greet("raunak")
