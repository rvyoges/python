#Write a program to find sum of all even numbers between 1 to n.
num=int(input())
sum=0
for i in range(1,num):
  if(i%2!=0):
    sum=sum+i
print(sum)
