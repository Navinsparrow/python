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
    
