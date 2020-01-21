# Print Hello World 
# Calculate Sum of Two Numbers
# Calculate SI
# Calculate Compound Interest
# Area of Circle 
# Distance b/w two points
# Check the given no. is even or odd.
# CHeck the given no. is postive, Negative or Zero 
# Largest of three numbers
# Smallest of three numbers
# Make a Calculator
# To check the type of the variable 
# Check the year is leap or not 
# Print ASCII value of character 
# Swap two numbers 
# Check No. is prime or not
# Number is Armstrong 
# Number is palindrome or not
# Print the sum of digits of a Number 
# Print sum of squares of first N Natural Numbers
# Print Cube Sum of squares of first N Natural Numbers
# Sum of even numbers upto N
# Sum of odd numbers upto N
# Print Fabonacci Series upto N
# Print the factorial of a Number

#//add two numbers using cmd argument
# WAP add.py that takes two numbers as command line arguments and print their sum
# WAP that prints the decimal equivalent of 1/2,1/3,1/4.....1/10 using for loop
# WAP that asks the user for a number and prints a countdown from that no. to zero using while loop
# 
# vission mission
# 2 black
# python intro 
# datatypes in python 

# 2 programs in one page
# Program 1: 
# 
# explain if else before program
# 
# explain loop before using
#  


print("Hello World\n")

a=int(input('Enter 1st No.: '))
b=int(input('Enter 2nd No.: '))
print("Sum is : ",a+b)

p=int(input('\nEnter P:'))
r=int(input('\nEnter R:'))
t=int(input('\nEnter T:'))
print("Simple Interest is :",p*r*t/100)

p1=int(input('\nEnter P:'))
r1=int(input('\nEnter R:'))
t1=int(input('\nEnter T:'))
n1=int(input('\nEnter N:'))
print("Compound Interest is :",p1*(1+r1/n1)**(n1*t1))

radius=int(input('Enter Radius of Circle: '))
print("Area of circle is: ",3.14*radius*radius)

import math
p1x=int(input("Enter X Coordinate of First point "))
p1y=int(input("Enter Y Coordinate of First point "))
p2x=int(input("Enter X Coordinate of Second point "))
p2y=int(input("Enter Y Coordinate of Second point "))
print("Distance b/w two points is: ",math.sqrt((p2x-p1x)*(p2x-p1x)+(p2y-p1y)*(p2y-p1y)))

eveodd=int(input('Enter a Number: '))
if eveodd%2==0:
    print("No. is Even")
else:
    print("No. is odd")

pnz=int(input('Enter a Number: '))
if pnz==0:
    print("No. is zero")
elif pnz>0:
    print("No. is +ve")
elif pnz<0:
    print("No. is -ve")

mxno=input('Enter three no.').split()
print("Max and Min of the Numbers are: ",max(int(mxno[0]),int(mxno[1]),int(mxno[2])),min(int(mxno[0]),int(mxno[1]),int(mxno[2])))

print("******* Calculator *******")
i1=int(input('Enter 1st No. '))
i2=int(input('Enter 2nd No. '))
ch=int(input('Enter Choice/n1.Add\n2.Subtract\n3.Multiply\n4.Division\n'))

if ch==1:
    print("Addition is ",i1+i2)
elif ch==2:
    print("Subtraction is ",i1-i2)
elif ch==3:
    print("Multiplication is ",i1*i2)
elif ch==4:
    print("Division ",i2/i1)


var=input("Enter a variable: ")
print("Type of Variable is: ",type(var))



year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

ci = input('Enter a Character')
print("The ASCII value of '" + ci + "' is", ord(ci))

no1=int(input('Enter 1st No. '))
no2=int(input('Enter 2nd No. '))
no1,no2=no2,no1
print("After Swapping: ",no1,no2)


num = int(input("Enter a number: "))
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")




num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



# **************Palindrome**************
n=int(input("Enter number:"))
n=str(n)

for i in range(0,len(n)):
    if n[i]==n[len(n)-1-i]:
        flag=1   
    else:
        flag=0
        break
if flag==1:
    print("Palindrome !")
else:
    print("Not Palindrome !")


# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")


n=int(input("Enter number:"))
s=0
for i in range(1,n+1):
   s=s+i
print("Sum of N number is: ",s) 


n=int(input("Enter number:"))
s=0
for i in range(1,n+1):
   s=s+i*i
print("Sum of squares of N number is: ",s) 


n=int(input("Enter number:"))
s=0
for i in range(1,n+1):
   s=s+i*i*i
print("Sum of cube of N number is: ",s) 




nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1



num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


