#function
# def is_composite(num,fcount=0):
#     for fa in range(1,num+1):
#         if num%fa==0 :
#             fcount+=1
#     return fcount>2
# print(is_composite(5))

# num=45
# fcount=0
# for fa in range(1,num+1):
#     if num%fa==0:
#         fcount+=1
# print('composite' if fcount>2 else 'non composite')

#recursion
# def fa_count(num,fa=1):
#     if fa==num:
#         return 1
#     return (num%fa==0)+fa_count(num,fa+1)
# def composite(num):
#     return fa_count(num)>2
# print(composite(6))


