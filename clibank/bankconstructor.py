class  bankconc:
    def __init__(self,balance=0,transfer=0,deposit=0,withdrawl=0,description=""):
        self.balance=balance
        self.transfer=transfer
        self.deposit=deposit
        self.withdrawl=withdrawl
        self.description=description
    def __str__(self):
      return f'{self.balance},{self.transfer},{self.deposit},{self.withdrawl},{self.description}'

    
    
