# num=13
# copy=num
# rev=0
# fcount1,fcount2=0,0
# while num!=0:
#     rev=rev*10+num%10
#     num//=10
# for fa in range(1,copy+1):
#     if(copy%fa==0):
#         if fcount1==2:
#             fcount1+=1
# for fa in range(1,rev+1):
#     if(rev%fa==0):
#         if fcount2==2:
#             fcount2+=2
# print ('emirp' if copy!=rev and fcount1==2 and fcount2==2 else 'not emirp')

#function
def reverse(num):
    rev=0
    while num!=0 :
        rev=rev*10+num%10
        num//=10
    return rev
def pallindrome(num):
    return num!=reverse(num)
def prime(num):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0 :
            fcount+=1
    return fcount==2
def rev_prime(num):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0 :
            fcount+=1
    return fcount==2
def is_emirp(num):
    return pallindrome(num) and prime(num) and rev_prime(num)
print(is_emirp(151))