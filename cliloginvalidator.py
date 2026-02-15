# 'userlogin'\
import re
import hashlib
import getpass

# string checker
def name(p):
        while True:
              if(re.fullmatch(r'[A-Za-b]$',p,re.I)):
                     return p
              else:
                     k=input('Invalid name format: ')
                     if (re.fullmatch(r'[A-Za-z]$',k,re.I)):
                            
                            
                            return 
# agechecker
def ager(n):
       while True:
        try:
                k= int(n)
                if(k>=1):
                          return k
                else: 
                                   k=int(input('invalid Age: ') )
                                   if (k >= 1):
                                           break 
        except ValueError:
                 k=input('invalid Age: ')
            

# emailcehcker
def checkemail(email):
       while True:
              if(re.fullmatch(r'[A-Za-b0-9]+@gmail.com$',email,re.I)):
                     return email
              else:
                     k=input('Invalid email: ')
                     if (re.fullmatch(r'\w+@gmail.com$',k)):
                            
                            return k

# passwordchecker
def psdconfirm(t=""):
      con=input('confirm password: ')
      while t!=con:     
                 con=input('invlaid password: ')
      return con

# temporal database
database=[]

# loop runeer
while True:
       firstname=name(input('First Name: '))
       lastname=name(input('Last Name: ').capitalize())
       email=checkemail(input('enter a valid email: ')).lower()
       temppassword=input('create passeord: ')
       confrimedpassword=psdconfirm(temppassword)
       age=ager(input('Age: '))
       gender=input('Gender-Male/Female: ').capitalize()

       user={'UserName': [firstname,lastname],
     'Email':email,

     'Userpassword':hashlib.sha256(confrimedpassword.encode()).hexdigest(),
      'userage':age,
      'usergender':gender
     }
       database.append(user)
       anotherinput=input('Do  you want to input any other user(y/n):  ').capitalize()
   
       if(anotherinput != 'Y'):
              break   



print(database)

       
    


        




       
             
             



              
     