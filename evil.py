num=13
count=0
while num!=0 :
    rem=num%2
    if rem==1 :
        count+=1
    num//2
print('evil' if count%2==0 else 'not evil')