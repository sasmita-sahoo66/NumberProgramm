# def remove_duplicates(st1):
#     new_s=''
#     while st1!='':
#         new_s+=st1[0]
#         st1=st1.replace(st1[0],'')
#     return new_s
# st1='engineering'
# print(remove_duplicates(st1))

# def remove_duplicates(st1):
#     new_s=''
#     for ch in new_s:
#         if ch not in new_s:
#             new_s+=ch
#     return new_s
# st1='enginnering'
# print(remove_duplicates(st1))


# def remove_duplicates(st1):
#     new_s=''
#     while st1!='':
#         new_s+=st1[0]
#         st1=st1.replace(st1[0],'')
#     return new_s
# st1='ababababab'
# print(remove_duplicates(st1))

# def remove_duplicates(l):
#     new_l=[]
#     for ch in l:
#         if ch not in new_l:
#             new_l+=ch
#     return new_l
# l=['s','a','s','m','i','t','a']
# print(remove_duplicates(l))

# def duplicates(st):
#     new_s=''
#     for ch in st:
#         if st.count(ch)>1:
#             new_s+=ch
#     return new_s
# st='engineering'
# print(duplicates(st))

def unique(st1):
    new_s=''
    for ch in st1:
        if st1.count(ch)==1:
            new_s+=ch
    return new_s
st1='sasmita'
print(unique(st1))






       
    