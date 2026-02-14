import re
# from cgpacalc import grade
import sys

def emailchecker(n):
     
     while True:
         if(re.search(r'\w+@gmail.com$',n) ):
             print('true')
             sys.exit()
         if not(re.search(r'\w+@gmail.com$',n)):
           
          k= input('what ypur email guy: ')
          if(re.search(r'\w+@gmail.com$',k)):
              print('Trueee')
              break
         
     
    
        
        
       

   
   
   
 


# def main():
#     check_grade()
# def check_grade():
#     assert grade('A')==5


# # if __name__ == "__main__":
# #     main


email=emailchecker(input('what your email: '))

