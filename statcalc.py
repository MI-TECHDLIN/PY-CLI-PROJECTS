import statistics

def main():
    
    # mean()
    question(i)
    moreq()
  

while True:
   input('hello welocome to your personal stat calc: press enter key to enter')
   i=input('what do you want to calculate today? \n A: Mean \n B: Median \n C: Mode \n')
   break

# Todo:next update more impolementaions in conditionaals
def question(q):
   if q == 'a':
      return  mean(int(input('how many input do you want? ')))
   elif q == 'b':
      return median(int(input('list the number you want to calculate? ')))
   elif q == 'c':
      return mode(int(input('what number do you want to get the most common number')))
   

def moreq():
     s=input('Any other Caluclations? y / n ')
     
     if s=='y':
      question(i)
   
      
# for mean
# more update would be added in my susbsequent commit
# -fractional mean
# -harmonic mean
# -geometric mean
def mean(q):
    r=[]
    for i in range(q):
     r.insert(1,float(input(f'{i+1}:  ')))
    return print(sum(r[:])/len(r))

# for mean
# more update would be added in my susbsequent commit
def median(p):
    r=[]
    for i in range(p):
     r.insert(1,float(input(f'{i+1}:  ')))
    return print(statistics.median(r[:]))

# for mean
# more update would be added in my susbsequent commit
def mode(k):
    r=[]
    for i in range(k):
     r.insert(1,float(input(f'{i+1}:  ')))
    return print(statistics.mode(r[:]))
  
# todo:graph,histogram and piechart feature

        
      

  

      
      

   

    
   




main()


# def meann(k):
      