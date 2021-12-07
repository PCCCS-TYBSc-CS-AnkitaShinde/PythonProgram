# Python program to display Fibonacci series
# To display Fibonacci series

num = int(input("Enter how many number you want to display:"))
a = 0
b = 1
c = 2
print("Fabonacci Series is")
print(a)
print(b)
while(c<num):
   d = a + b
   print(d)
   a = b
   b = d
   c += 1

# Python program to print sum of digits
#sum of digits
n=int(input("Enter a number:"))
sum = 0
while(n>0):
    rem = n%10
    sum = sum + rem
    n=int(n/10)
print("The sum of digits is:",sum)



# Python program to reverse a number
# Reverse of a number
n = int(input("Enter the number: "))
rev = 0
while (n > 0):
    rem = n % 10
    rev = (rev * 10) + rem
    n = int(n/10)
print("Reverse of number is :",rev)


# Python program to check whether the number is an Armstrong number or not

n = int(input("Enter a number: "))
num = n
sum = 0

while n > 0:
   rem = n % 10
   sum = sum+rem*rem*rem
   n=int(n/10)
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Python program to check givaen number is prime or not
# given number is prime or not
n = int(input("Enter a number:"))
for i in range(2,n+1):
   if n % i == 0:
      break
if i == n:
   print(n,"is prime number")
else:
   print(n,"is not a prime nmber")

#Python program to print all even number between 1 and 100
# All even number between 1 and 100
sum = 0
for i in range(0,101,2):
   print(i)
   sum = sum + i
print("Sum of Even numbers=",sum)

# Program to display pyramid

for i in range(1,6):
   for j in range(1,i+1):
      print(j,end=' ')
   print()

# Program to display pyramid

count = 1
for i in range(1,6):
   for j in range(1,i+1):
      print(count,end=' ')
   count = count +1
   if count > 9:
      count = 1
   print()
# Program to display pyramid

count = 1
for i in range(1,5):
   for j in range(1,i+1):
      print(count,end=' ')
      count=count+1
   print()

# Program to display pyramid

for row in range(1,5):
   for sp in range(1,5-row):
      print(' ',end=' ')
   for col in range(1,row+1):
      print(col, end=' ')
   for erow in range(col-1,0,-1):
      print(erow,end=' ')
   print()
