num=192
s=str(num**1)+str(num**2)+str(num**3)
for n in range(1,10):
    if str(n) not in s:
        print('not fascinating')
        break
else:
    print('fascinating')
