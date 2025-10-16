num=int(input("enter the nuber:"))
temp=num
sum=0       
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an armstrong number") 
else:
    print(num,"is not an armstrong number")