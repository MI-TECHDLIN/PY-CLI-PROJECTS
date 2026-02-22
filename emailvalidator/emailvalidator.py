import re
import emailclass
# email checker
class emailvalid:
      def name(self):
         while True:
              if(re.match(r'[A-Za-z]+$',self,re.I)):
                     return self
              else:
                     k=input('Invalid name format: ')
                     if (re.match(r'[A-Za-z]',k,re.I)):
                              return k   
# agechecker
      def ager(self):
             while True:
              try:
                   k= int(self)
                   if k and k>=1:
                           return k
                   else: 
                         self =input('Age is less than 1: ')
              except ValueError:
                self=input('invalid Age format: ')
            #     if (s):
            #           return s

                   
# emailcehcker
      def checkemail(self):
          while True:
              if(re.fullmatch(r'[A-Za-b0-9]+@gmail.com$',self,re.I)):
                     return self
              else:
                     k=input('Invalid email: ')
                     if (re.fullmatch(r'\w+@gmail.com$',k)):
                            
                            return k
# passwordchecker
      def psdconfirm(self=""):       
           con=input('confirm password: ')
           while self!=con:     
                 con=input('invlaid password: ')
           return con
#defaultinit
      @classmethod
      def getuserdetails(cls):
         while True:
            firstname=emailvalid.name(input('First Name: '))
            lastname=emailvalid.name(input('Last Name: '))
            email=emailvalid.checkemail(input('enter a valid email: '))
            temppassword=input('create passeord: ')
            confrimedpassword=emailvalid.psdconfirm(temppassword)
            age=emailvalid.ager(input('Age: '))
            gender=input('Gender-Male/Female: ')

            getall=emailclass.Emailconstructor(firstname,lastname,email,temppassword,confrimedpassword,age,gender)
         
         
       
            return getall.todict()
