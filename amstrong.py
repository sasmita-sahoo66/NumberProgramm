# num=123
# copy=num
# dsum=0
# count=len(str(num))
# while num!=0:
#     ld=num%10
#     dsum+=ld**count
#     num//=10
# print('amstrong' if copy==dsum else 'not amstrong')

#function
# def is_sumfact(num):
#     copy=num
#     dsum=0
#     count=len(str(num))
#     while num!=0:
#         ld=num%10
#         dsum+=ld**count
#         num//=10
#     return copy==dsum
# def is_amstrong(num):
#     return is_sumfact(num)
# print(is_amstrong(153))

# Recursion

def dig_sum(num,count):
   
    if num==0:
        return 0
    return (num%10)**count+dig_sum(num//10,count)
def amstrong(num):
    return num==dig_sum(num,len(str(num)))
print(amstrong(371))

