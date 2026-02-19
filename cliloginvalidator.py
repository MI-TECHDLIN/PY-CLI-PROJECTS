# 'userlogin'\
import re
import hashlib
import getpass
import json

class jsonfile:
      def loadfile(self):
            try:
                  with open(self,'r') as self:
                        return json.load(self)
            except FileNotFoundError,json.JSONDecodeError:
                  return['file not found']
            
      def savefile(self,file):
            with open(file,'w') as file:
                  return json.dump(self,file,indent=1)
       

# string checker
class emailvalidator:
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
                   if(k>=1):
                          return k
                   else: 
                                   k=int(input('invalid Age: ') )
              except ValueError:
                n =input('invalid Age format: ')

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

class Emailconstructor:
        def __init__(self,firstname,lastname,email,temppassword,confirimpasssword,age,gender):
              self.firstname=firstname
              self.lastname=lastname
              self.email=email
              self.temppass=temppassword
              self.confrimpass=confirimpasssword
              self.age=age
              self.gender=gender

        def todict(self):
           return{'UserName': {'firstname':self.firstname,'secondname':self.lastname},
     'Email':self.email,

     'Userpassword':hashlib.sha256(self.confrimpass.encode()).hexdigest(),
      'userage':self.age,
      'usergender':self.gender
     }
                    
              



def getuserdetails():
        rvalid=emailvalidator
        while True:
         firstname=rvalid.name(input('First Name: '))
         lastname=rvalid.name(input('Last Name: '))
         email=rvalid.checkemail(input('enter a valid email: '))
         temppassword=input('create passeord: ')
         confrimedpassword=rvalid.psdconfirm(temppassword)
         age=rvalid.ager(input('Age: '))
         gender=input('Gender-Male/Female: ')

         getall=Emailconstructor(firstname,lastname,email,temppassword,confrimedpassword,age,gender)
         
         
       
         return getall.todict()
        


# loop runeer
def main():
       file='userdashboard.json'
       jsondbs=jsonfile
       dbs=jsondbs.loadfile(file)
       dbs.append(getuserdetails())
       jsondbs.savefile(dbs,file)
       
      
       

       
        
       # database.append(user)
       # anotherinput=input('Do  you want to input any other user(y/n):  ').capitalize()
   
       # if(anotherinput != 'Y'):
       #        break   

if __name__ == "__main__":
      main()



       
    


        




       
             
             



              
     