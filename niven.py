# num=325
# dsum=0
# copy=num
# while num!=0:
#     dsum+=num%10
#     num//=10
# print('niven' if copy==num else 'not niven')

#function
# def sum_dig(num):
#     dsum=0
#     while num!=0:
#         dsum+=num%10
#         num//=10
#     return dsum
# def is_niven(num):
#     return num%sum_dig(num)==0
# print(is_niven(12))
# print(is_niven(325))

#recursion
def sum_dig(num):
    if num==0:
        return 0
    return (num%10)+sum_dig(num//10)
def niven(num):
    return num%sum_dig(num)==0
print(niven(12))