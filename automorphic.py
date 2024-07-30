# num=234
# rem=0
# squar=num**2
# count=len(str(num))
# rem=squar%(10**count)
# print ('automorphic' if num==rem else 'not automorphic')

#Function

def is_rem(num):
    count=len(str(num))
    squar=num**2
    rem=squar%(10**count)
    return num==rem
def is_automorphic(num):
    return is_rem(num)
print(is_automorphic(5))