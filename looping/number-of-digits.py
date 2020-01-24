#Write a program to count number of digits in a number.
num=int(input())
count=1
while(num//10!=0):
  num=num//10
  count=count+1
print(count)
