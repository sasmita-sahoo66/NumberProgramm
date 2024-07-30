import re
s='sasmita Sahoo And come From BhubaNeswar'
#a=re.findall('[a-z]',s)
a=re.findall('[a-zA-z]',s)
print(' '.join(a))