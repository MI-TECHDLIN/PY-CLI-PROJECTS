from bankconstructor import bankp

balance=2500

def userrequest():
    bank=bankp(balance=balance)
    
    print(f'_________________(((((((Welcome to Cli Banking)))))))_______________')
    
    user=input('what do you want to do today \n Press: \n T - Transfer \n D - Depsoit \n W - Withdrawl\n B - Check Balance (: ' )


   
    
    
    
   
    
    while True:
        if user == 't':
           transfer=int(input('how much do you want to Transfer: '))
           r=bank.transfer(transfer,'dddd')
           print(r)
        elif user == 'd':
          deposit=int(input('how much do you want to Deposit: '))
          print(bank.deposit(deposit))
        elif user == 'w':
           withdrawl=int(input('how much do you want to Withdrawl: '))
           print(bank.withdrawl(withdrawl))
        elif user == 'b':
         print(bank.balance)

        d= input('do you want to proccess anything? y/n').lower()
        if not d == 'y':
         break



    

     


def main():
    userrequest()
    

    
    










if __name__ == '__main__':
    main()