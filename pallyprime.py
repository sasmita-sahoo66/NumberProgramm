# num=12321
# copy=num
# rev=0
# fcount=0
# for fa in range(1,copy+1):
#     if copy==fa:
#         fcount+=1
# while num!=0:
#     rev=rev*10+num%10
#     num//=10
# print('pallyprime' if copy==num else'not pallyprime')

#function
def is_rev(num):
    copy=num
    rev=0
    while num!=0:
        rev=rev*10+num%10
        num//=10
    return copy
def is_prime(num):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
def is_pallyprime(num):
    return is_rev(num) and is_prime(num)
print(is_pallyprime(123))