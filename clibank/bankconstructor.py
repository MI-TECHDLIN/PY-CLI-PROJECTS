balance=200

class bankp:
    def __init__(self,balance=0,transfer=0,deposit=0,withdrawl=0,description=""):
        self.balance=balance
        self.transfer=transfer
        self.deposit=deposit
        self.withdrawl=withdrawl
        self.description=description
   

            
def transfer(transferamount,description):
        bank=bankp(balance=balance,transfer=transferamount,description=description)
        suce=bank.balance - bank.transfer
        return suce,bank.description


        

   

        

def main():
    amount,description=transfer(transferamount=20,description='for daddy')

    print(f'Balance: ${amount}, Description: {description}',)













if __name__ == '__main__':
    main()