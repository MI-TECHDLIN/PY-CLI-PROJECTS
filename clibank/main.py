balance=2500

from bankconstructor import bankconc


def userrequest(): 
    print(f'_________________(((((((Welcome to Cli Banking)))))))_______________')
    global balance
    bank=bankconc(balance)
  
    
    while True:
           
              user=input('what do you want to do today \n Press: \n T - Transfer \n D - Depsoit \n W - Withdrawl\n B - Check Balance (: ' )
        
            #   transfer
              if user == 't':
               transfe=int(input('how much do you want to Transfer: '))
               transfdes=input('Description: ')
               print(r:=bank._transfer(transfe,transfdes))
               
            
            #  deposit
              elif user == 'd':
               deposit=int(input('how much do you want to Deposit: '))
               print(r:=bank._deposit(deposit))
               

            #   withdraw
              elif user == 'w':
               withdrawl=int(input('how much do you want to Withdrawl: '))
               print(r:=bank._withdrawl(withdrawl))


            #   checkbalance
              elif user == 'b':
               print(bank._balance),
          

              
              if  (d:= input('do you want to process anything? y/n: ').lower()) !='y':
               break
            

           
        

   



    

     


def main():
    userrequest()
    

    
    










if __name__ == '__main__':
    main()