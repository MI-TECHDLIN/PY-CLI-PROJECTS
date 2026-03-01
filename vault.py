class Vault:
    def __init__(self,galleons=0,sickeles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickeles
        self.knuts=knuts
    def __str__(self):
        return  f'Gallenos: {self.galleons}, Sickles: {self.sickles}, Knuts: {self.knuts}'
    def __add__(self,other):
        gall=self.galleons + other.galleons
        sick=self.sickles + other.sickles
        knut=self.knuts + other.knuts
        return Vault(gall,sick,knut)
    
    
pott=Vault(100,50,25)
print(pott)


weas=Vault(25,50,100)
print(weas)
weas=Vault(25,50,100)
print(weas)
total=pott+weas
print(total)

# total =set()

# total.add('djdj')

# print(total)