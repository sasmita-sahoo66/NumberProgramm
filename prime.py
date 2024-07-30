#function
# def is_prime(num,fcount=0):
#     for fa in range(1,num+1):
#         if num%fa==0 :
#             fcount+=1
#     return fcount==2
# print(is_prime(5))

# num=45
# fcount=0
# for fa in range(num,num+1):
#     if num%fa==0:
#         fcount+=1
# print('prime' if fcount==2 else 'non prime')

#recursion
def fa_count(num,fa=1):
    if fa==num:
        return 1
    return (num%fa==0)+fa_count(num,fa+1)
def prime(num):
    return fa_count(num)==2
print(prime(19))