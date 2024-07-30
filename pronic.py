# num=12
# n=0
# while n*(n+1)<num :
#     n+=1
# print('pronic' if num==n*(n+1) else 'not pronic')

# def is_pronic(num):
#     n=0
#     while n*(n+1)<num :
#         n+=1
#     return num==n*(n+1)
# print(is_pronic(12))

#recursion
def is_pronic(num,n=1):
    if n*(n+1)==num :
        return 1
    return n > num //2 
def pronic(num):
    return is_pronic(num)
print(is_pronic(6))
print(is_pronic(12))