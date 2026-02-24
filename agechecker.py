class age:
    def __init__(self,age):
        if age <= 0:
            raise ValueError('invalid age oga')
    
        self.age=age
    def __str__(self):
        return self.age     
        
class student(age):
    def __init__(self,classs,age):
        super().__init__(age)
        self.classs=classs
    def __str__(self):
        return f'{self.classs},{self.age}'    
   
        
class pupils(age):
    def __init__(self,classs,age):
        super().__init__(age)
        self.classs=classs
    def __str__(self):
        return [self.classs,self.age]     
   
        
    




student=pupils('name',0)
print(student)