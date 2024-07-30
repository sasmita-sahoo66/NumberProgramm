# num=12321
# rev=0
# copy=num
# while num!=0:
#     ld=num%10
#     rev=rev*10+ld
#     num//=10
# print('pallindrome' if copy==rev else 'not pallindrome')

#function
def is_rev(num,rev=0):
    copy=num
    while num!=0:
        rev=(rev*10)+(num%10)
        num//=10
    return copy==rev
def is_pallindrome(num):
    return is_rev(num)
print(is_pallindrome(123))
print(is_pallindrome(323))

#recursion
def reverse(num,rev=0):
    if num==0:
        return rev
    return reverse(num//10,rev*10+(num%10))
def pallindrome(num):
    return num==reverse(num)
print(pallindrome(343))
    