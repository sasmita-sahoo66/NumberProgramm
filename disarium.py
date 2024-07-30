# num=23
# copy=num
# dsum=0
# count=len(str(num))
# while num!=0:
#     ld=num%10
#     dsum+=ld**count
#     num//=10
      #count-=1
# print('disarium' if copy==dsum else 'not disarium')

#function
# def is_sumfact(num):
#     copy=num
#     dsum=0
#     count=len(str(num))
#     while(num!=0):
#         ld=num%10
#         dsum+=ld**count
#         num//=10
#     return copy==dsum
# def is_disarium(num):
#     return is_sumfact(num)
# print(is_disarium(153))

#recursion
def dig_sum(num,count):
    if num==0:
        return 0
    return (num%10)**count+dig_sum(num//10,count-1)
def disarium(num):
    return num==dig_sum(num,len(str(num)))
print(disarium(135))

