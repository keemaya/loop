num=371
m=num
sum=0
while sum>0:
    sum=sum+(num%10)(num%10)(num%10)
    num=num//10                     
if m==num:
    print(num,"it is armstrong number")
else:
    print(num,"it is not armstrong number")