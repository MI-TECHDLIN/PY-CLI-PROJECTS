class  bankconc:
    def __init__(self,_balance=0,):
        self._balance=_balance

    # def checkbalance(self,b):
    #     self._balance=b
    #     return self._balance
    # transferfunc
    def _transfer(self,t,d=''):
        self._balance-=t
        return self._balance,d
    
    # deposit
    def _deposit(self,de,d=''):
        self._balance+=de
        return self._balance,de
    
    # withdrawlfunc
    def _withdrawl(self,w,d=''):
        self._balance-=w
        return self._balance,w
    
 
       
        
    


    
    
