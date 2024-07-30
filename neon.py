# def is_num(num):
#     square=num**2
#     dsum=0
#     while square!=0 :
#         dsum+=square%10
#         square//=10
#     return num==dsum
# def is_neon(num):
#     return is_num(num)
# print(is_neon(9))
num=9
sqr=num**2
dsum=0
count=len(str(num))
while sqr!=0 :
    ld=sqr%10
    dsum+=ld 
    sqr//=10
    if num==dsum :
        print('neon')
    else:
        print('not neon')
