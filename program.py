# perform input/output of all basic data types
a=int(input("enter the number to be print:"))
print(a)
b=str(input("enter the string to be print:"))
print(b)
c=float(input("enter the float number to be print"))
print(c)
d=complex(input("enter the complex number to be print:"))
print(d)

# to find the sum
e=int(input("enter the number:"))
f=int(input("enter the number:"))
print(e+f)

# perform all arithmetic opertation
g=int(input())
h=int(input())
print=(g+h,g-h,g*h,g//h,g**h,g/h)

# perimeter of rectangle
i=int(input("enter the lenght of the rectangle:"))
j=int(input("enter the width of the rectangle:"))
print(2*(i+j))

# area of the rectangle
l=int(input("enter the lenght of the rectangle:"))
k=int(input("enter the width of the rectangle:"))
print(k*l)

# find its diameter, circumference and area of circle
pi=3.14
r=int(input("enter the radius of the circle:")) 
di=2*r
cr=2*pi*r
ar=2*pi*r**2
print("the diameter of the circle is",di)
print("the circumference of the circle is",cr)
print("the area of the circle is",ar)

# cm to meters and km
cm=int(input("enter the centimeter:"))
meter=cm/100
km=cm/100000
print("meter=",meter)
print("kilometer=",km)

# Celsius  into Fahrenheit. 
cel=int(input("enter the tempature in celsius:"))
fah=(cel*9/5)+32
print("Fahrenheit=",fah)

# Fahrenheit into Celsius
fa=int(input("enter the tempature in fahrenheit:"))
ce=(fa-32)*5/9
print("celsius=",ce)

# convert days into years, weeks and days.
day=7
da=int(input("enter the days"))
year=int(d/365)
week=int((d%365)/day)
days=(d%365)%day
print("year=",year)
print("weeks=",week)
print("days=",days)

# find power of any number x ^ y.
x=int(input("enter the number:"))
y=int(input("enter the number:"))
print(x**y)

# enter any number and calculate its square root.
num=int(input("enter the number:"))
sqr=n**0.5
print("square root=",sqr)

# enter two angles of a triangle and find the third angle.
a1=int(input("enter first angle:"))
a2=int(input("enter second angle:"))
a3=180-(a1+a2)
print("third angle:",a3)

# enter base and height of a triangle and find its area
base=int(input("enter the base"))
height=int(input("enter the height"))
area=(base*height)/2
print("area of the tringle=",area)

#  calculate area of an equilateral triangle. 
s=int(input())
ae=((3**0.5)/4)*(s*s)
print(ae)

#  enter marks of five subjects and calculate total, average and percentage. 
s1,s2,s3,s4,s5=map(int,input(),split(" "))
ave=(s1+s2+s3+s4+s5)/5
tol=s1+s2+s3+s4+s5
pec=(t/500)*100
print("average=",ave;"total=",tol;"pec=",pec)

#  enter P, T, R and calculate Simple Interest.
P=float(input("Enter the principle amount : "))
R=float(input("Enter the rate of interest : "))
T=float(input("Enter the time in the years: "))
si=(P*R*T)/100
print("simple interest",si)

# enter P, T, R and calculate Compound Interest. 
p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))
ci =  p * (pow((1 + r / 100), t)) 
print("compound interest :", ci)



c1=int(input("enter the number"))
c2=int(input("enter the number"))
if(c1>c2):
    print(c1)
else:
    print(c2)  

# find maximum between three numbers
b1=int(input("enter the number"))
b2=int(input("enter the number"))
b3=int(input("enter the number"))
if(b1>b2)and(b1>b3):
    print(b1)
elif (b2>b1)and(b2>b3):
    print(b2)
else:
    print(b3)     


# reverse string using recusion
def rev(s):
    str=" "
    for i in s:
        str=i+str
     return str
    num=str(input("enter the string:"))
    print(rev(num).end="")  

#  Fibonacci series using recusion
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-1))
 fibb=int(input("enter the number"))
  if fibb>0:
     for i in range(0,fibb+1)
         print(fib(i),end="")

# palindrome(string) using recursion
def palindrome(s)
 if len(s)<1:
     return True
 else:
     if s[0]==s[-1]:
         return palindrome(s[1:1])
     else:
         return False            
palin=str(input(""))
if(palindrome(palin)==True)
  print("yes")
else:
    print("no")  

# palindrome(number) using recursion
number=int(input("Enter number:"))
temp=number
rev=0
while(number>0):
    div=number%10
    rev=rev*10+div
    number=number//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

# factorial using recursion
def fact(n):
    if(n==1):
        return 0
    else:
        return n*fact(n-1)
fac=int(input())
if (fac<0):
    print("pls enter the positive number")
elif (fac==0):
    print(fac)
else:
    print(fact(fac))

# count the array element
cc=["a","a","b","b","b","a"]
dd=[i:cc.count(i) for i in cc]
print(dd)

# check whether a number is negative, positive or zero.
num = int (input())
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")

# check whether a number is divisible by 5 and 11 or not. 
number = int(input())
if((number % 5 == 0) and (number % 11 == 0)):
    print("Divisible by 5 and 11".format(number))
else:
    print("Not Divisible by 5 and 11".format(number)) 

# check whether a number is even or odd.
even=int(input("enter the number:"))
if(even % 2 == 0):
    print("even")
else:
    print("odd")

# check whether a year is leap year or not.
year = int (input(""))

if((year%400 ==0)or(year%4 ==0)&(year%100!=0)):
  print("yes")
else:
  print("no") 

#   check whether a character is alphabet or not
li = input("")
if l in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
	    print("Alphabet")
else:
	    print("No")

# input any alphabet and check whether it is vowel or consonant. 
lis = input("")
if l in('a', 'e', 'i', 'o', 'u'):
	    print("Vowel")
else:
	    print("Consonant")

#   input any character and check whether it is alphabet, digit or special character. 
ch = input("Enter Your letter : ")
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is a Special Character") 

# check whether a character is uppercase or lowercase alphabet.
chr = input("Enter Your letter : ")
if(chr.isupper()):
    print("The Given Character ", chr, "is an Uppercase Alphabet")
elif(ch.islower()):
    print("The Given Character ", chr, "is a Lowercase Alphabet")
else:
    print("The Given Character ", chr, "is Not a Lower or Uppercase Alphabet")          

# input week number and print weekday
weekNumber = input("Enter the week number:")
weekNumber = int(weekNumber)
if (weekNumber == 1):
  weekDay = "Saturday"
elif (weekNumber == 2):
  weekDay = "Sunday"
elif (weekNumber == 3):
  weekDay = "Monday"
elif (weekNumber == 4):
  weekDay = "Tuesday"
elif (weekNumber == 5):
  weekDay = "Wednesday"
elif (weekNumber == 6):
  weekDay = "Thursday"
elif (weekNumber == 7):
  weekDay = "Friday"
else:
  weekDay = "Please enter the week number between 1 and 7"
  
print (weekDay)
   
# input month number and print number of days in that month. 
monthname = input("Input the name of Month: ")
 if monthname == "February":
	print("No. of days: 28/29 days")
elif monthname in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif monthname in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 

# count total number of notes in given amount
def no_notes(a):
  r = [500, 200, 100, 50, 20, 10]
  t = 0
  for i in range(6):
    q = r[i]
    t += int(a / q)
    a = int(a % q)
  if a > 0:
    t = -1
  return x
  note=int(input("enter the amount:"))
print(no_notes(note))
print(no_notes(note))

# input angles of a triangle and check whether triangle is valid or not.
c1 = int(input('Please Enter the First Angle of a Triangle: '))
c2 = int(input('Please Enter the Second Angle of a Triangle: '))
c3 = int(input('Please Enter the Third Angle of a Triangle: '))
total = c1 + c2 + c3
if total == 180:
    print("\nThis is a Valid Triangle")
else:
    print("\nThis is an Invalid Triangle")

# input all sides of a triangle and check whether triangle is valid or not.
def tri(x, y, z):   
    if (x + y <= z) or (x + z <= y) or (y + z <= x) : 
        return False
    else: 
        return True            
a = int(input())
b = int(input())
c = int(input())
if tri(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 

#  check whether the triangle is equilateral, isosceles or scalene triangle. 
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")

# program to find all roots of a quadratic equation.
import cmath
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
d = (b**2) - (4*a*c)
e = (-b-cmath.sqrt(d))/(2*a)
f= (-b+cmath.sqrt(d))/(2*a)
print(e,f)

# calculate profit or loss
a = float(input("Enter the Actual Product Price: "))
b = float(input("Enter the Sales Amount: "))
 if(a > b):
    amount = a - b
    print("Loss Amount = {0}".format(amount))
elif(b > a):
    amount = b - a
    print("Profit Amount = {0}".format(amount))
else:
    print("No Profit No Loss!!!")

#   Calculate percentage and grade 
a=int(input("enter the percentage"))
if(a>=90):
    print("grade:A")
elif(a>=80):      
    print("grade:B")
    elif(a>=70):      
    print("grade:C")
    elif(a>=60):      
    print("grade:D")
    elif(a>=40):      
    print("grade:E")
    else:
        print("grade:F")

# print day of week name using switch case. 
        def week(i):
        switcher={
                1:'Sunday',
                2:'Monday',
                3:'Tuesday',
                4:'Wednesday',
                5:'Thursday',
                6:'Friday',
                7:'Saturday'
             }
        return switcher.get(i,"Invalid day of week")
a= int(input())
print(week(a))

# print total number of days in a month using switch case        
def days(i):
        switcher={
                1:'31 days',
                2:'29 and 28 days',
                3:'31 days',
                4:'30 days',
                5:'31 days',
                6:'30 days',
                7:'31 days',
                8:'30 days',
                9:'31 days',
                10:'30 days',
                11:'31 days',
                12:'30 days'
             }
        return switcher.get(i,"Invalid month")
a= int(input("enter the in number:"))
print(days(a))

# check whether an alphabet is vowel or consonant using switch case. 
def letter(n):
        switcher={
                'a':'vowel',
                'e':'vowel',
                'i':'vowel',
                'o':'vowel',
                'u':'vowel'
             }
        return switcher.get(n,"consonant")
b= str(input("enter the in letter:").lower())
print(letter(b))

# print all natural numbers from 1 to n. - using while loop 
num = int(input("Please Enter any Number: "))
i = 1
while ( i <= num):
    print (i, end = '  ')
    i = i + 1

# print all natural numbers in reverse (from n to 1). - using while loop 
num = int(input("Please Enter any Number: "))
i = num 
while ( i >= 1):
    print (i, end = '  ')
    i = i - 1

#  print all even numbers between 1 to 100. - using while loop
x=1
y=100
for i in range(x,y):
    if(i%2==0):
        print(i,end=" ")    

# print all odd number between 1 to 100
x=1
y=100
for i in range(x,y):
    if(i%2!=0):
        print(i,end=" ")   

# find sum of all natural numbers between 1 to n
n = int(input("Enter Number to calculate sum"))
sum = 0
for num in range(0,n+1,1):
    sum = sum+num
print(sum)

# find sum of all even numbers between 1 to n.
n = int(input(" Please Enter the Maximum Value : "))
sum = 0
for i in range(1, n+1):
    if(i % 2 == 0):
        sum = sum + i
print(sum)

# find sum of all odd numbers between 1 to n. 
n = int(input(" Please Enter the Maximum Value : "))
sum = 0
for i in range(1, n+1):
    if(i % 2 != 0):
        sum = sum + i
print(sum)

#  print multiplication table of any number
n=int(input())
for i in range (1,10+1):
  print(n,"x",i,"=",n*i)

# count number of digits in a number.
n=int(input())
count=0
while(n>0):
    count=count+1
    n=n//10
print(count)
