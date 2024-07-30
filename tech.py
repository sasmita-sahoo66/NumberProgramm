# num=int(input('enter a number :'))
# count=len(str(num))
# first=num//(10**(count//2))
# last=num%(10**(count//2))
# if count%2==0 and (first+last)**2 :
#     print('tech number')
# else:
#     print('non tech')

def tech(num):
    count = len(str(num))
    first = num // (10 ** (count // 2))
    last = num % (10 ** (count // 2))
    return (first + last) ** 2 if count % 2 == 0 else None

print(tech(2025))

       