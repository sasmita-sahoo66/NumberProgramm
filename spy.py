# num=23
# dsum=0
# dprod=1
# while num!=0 :
#     ld=num%10
#     dsum+=ld
#     dprod*=1
#     num//=10
# print('spy'if dsum==dprod else 'notspy')

# function
# def dig_sum(num):
#     dsum=0
#     while num!=0 :
#         dsum+=num%10
#         num//=10
#     return dsum
# def dig_prod(num):
#     dprod=1
#     while num!=0:
#         dprod*=num%10
#         num//=10
#     return dprod
# def is_spy(num):
#     return dig_sum(num)==dig_prod(num)
# print(is_spy(15))

#recursion
def dig_sum(num):
    dsum=0
    if num==0:
        return 0
    return (num%10)+dig_sum(num//10)
def dig_prod(num):
    if num==0:
        return 1
    return (num%10)*dig_prod(num//10)
def spy(num):
    return dig_sum(num)==dig_prod(num)
print(spy(123))

