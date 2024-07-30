# num=145
# copy=num
# dsum=0
# while(num!=0):
#     ld=num%10
#     fact=1
#     for n in range(ld,0,-1):
#         fact*=n
#     dsum+=fact
#     num//=10
# print('strong' if copy==dsum else 'not strong')

#function
def is_sum(num):
    copy=num
    dsum=0
    while num!=0 :
        ld=num%10
        fact=1
        for n in range(ld,0,-1):
            fact*=n
        dsum+=fact
        num//=10
    return copy==dsum
def is_strong(num):
    return is_sum(num)
print(is_strong(145))