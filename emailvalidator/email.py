# 'userlogin'\
import jsonhandler
import emailvalidator


#  runeer
def main():
       file='userdashboard.json'
       jsondbs=jsonhandler.jsonfile
       dbs=jsondbs.loadfile(file)
       dbs.append(emailvalidator.emailvalid.getuserdetails())
       jsondbs.savefile(dbs,file)
       
      
       

       
        
       # database.append(user)
       # anotherinput=input('Do  you want to input any other user(y/n):  ').capitalize()
   
       # if(anotherinput != 'Y'):
       #        break   

if __name__ == "__main__":
      main()



       
    


        




       
             
             



              
     