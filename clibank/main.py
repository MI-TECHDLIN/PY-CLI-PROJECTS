from bankconstructor import bankconc
from bankfunction import bankfunc


def userrequest(): 
    print(f'_________________(((((((Welcome to Cli Banking)))))))_______________')
    balance=2500
    bank=bankconc(balance)
    func=bankfunc
    
    
    while True:
           
              user=input('what do you want to do today \n Press: \n T - Transfer \n D - Depsoit \n W - Withdrawl\n B - Check Balance (: ' )
        
              
              if user == 't':
               transfe=int(input('how much do you want to Transfer: '))
               transfdes=input('Description: ')
               bank.transfer=transfe
               bank.description=transfdes
               r=func.transfer(bank.balance,bank.transfer,bank.description)
               print(r)

              elif user == 'd':
               deposit=int(input('how much do you want to Deposit: '))
               print(bank.deposit(deposit))

              elif user == 'w':
               withdrawl=int(input('how much do you want to Withdrawl: '))
               print(bank.withdrawl(withdrawl))

              elif user == 'b':
               print(bank.balance),
          

              d= input('do you want to proccess anything? y/n').lower()
              if  d == 'y':
               break
            

           
        

   



    

     


def main():
    userrequest()
    

    
    










if __name__ == '__main__':
    main()