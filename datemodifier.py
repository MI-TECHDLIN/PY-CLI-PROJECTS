import re
# datemodifier
# txt='11-2-2008'

# kir=re.match('\d{2}+',txt,)
# print(kir.group())

txt='today is 23/02/2019.'\
'yesterday was 22/02/2019.'\
'januaru was 24/02/2019.'

p=re.compile('(\d{2})\/(\d{2})\/(\d{4})')
pE=p.sub(r'\3.\2.\1',txt)
print(pE)
