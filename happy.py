# def is_sum(num):
#     dsum=0
#     while num>9:
#         dsum=0
#         while num!=0:
#             ld=num%10
#             dsum+=ld**2
#             num//=10
#         num=dsum
#     return dsum
# def happy(num):
#     num=is_sum(num)
#     return num==1
# def is_happy(num):
#     return happy(num)
# num=int(input('enter a number'))
# print(is_happy(num))

num=44
# dsum=0
copy=num
while num>9:
    dsum=0
    while num!=0:
        ld=num%10
        dsum+=ld**2
        num//=10
    num=dsum
print('happy' if copy==1 else 'not happy')


