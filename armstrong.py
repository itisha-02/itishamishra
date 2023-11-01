num = int(input("Enter a number :"))
a = num
sum = 0
while (a!=0):
              digit = a % 10
              cube = digit**3
              sum = sum + cube
if (a==sum):
              print(a , "is an Armstrong number")
else :
              print(a , "is not an Armstrong number")
