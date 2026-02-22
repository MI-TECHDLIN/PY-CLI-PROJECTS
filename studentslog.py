import json
class Studentdashboaed:
    def __init__(self,firstname,secondname,age,classs,sex,bestsubject):
         self.firstname=firstname
         self.secondname=secondname
         self.age=age
         self.classs=classs
         self.sex=sex
         self.bestsubject=bestsubject
                          
    def todict(self):
        return {'firstname':self.firstname,
                     'secondname':self.secondname,
                     'age':self.age,
                     'class':self.classs,
                     'sex':self.sex,
                     'bestsubject':self.bestsubject},

    @classmethod
    def getstundent(cls):
         f=input('Firstname: ')
         s=input('Secondname: ')
         a=int(input('Age: '))
         c=input('Class: ')
         sex=input('Sex: ')
         b=input('Best subject: ')
         obsjectstundent=cls(f,s,a,c,sex,b)
         return obsjectstundent.todict()

# endofofunc
        




jsonfile='stundent.json'

def loadfile():
    try:
        with open(jsonfile, 'r') as  file:
            return json.load(file)
    except FileNotFoundError,json.JSONDecodeError:
        return['not found']

def savestt(student):
    with open(jsonfile,'w') as file:
        return json.dump(student,file,indent=1)
    

         
def main():
    student=loadfile()
    student.append(Studentdashboaed.getstundent())
    savestt(student)


if __name__ == '__main__':
     main()

  
