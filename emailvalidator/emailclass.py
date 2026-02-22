import hashlib
import getpass
# emailclass
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
       