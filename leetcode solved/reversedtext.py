s=input()
k=""
for r in reversed(s):
    if s[0::].capitalize():
         k+=r
    else:
         if r.isupper():
            k+=r.lower()

         elif r.islower():
            k+=r.upper()
print(k)
    
