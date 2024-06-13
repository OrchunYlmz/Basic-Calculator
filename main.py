#Calculator
from art import logo
#Add
def add(n1,n2):
  return n1+n2 

#Substract
def sub(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

#Root
def root(n1,n2):
  return (n1)**(1/n2)

#Exponential 
def expo(n1,n2):
  return n1**n2
  
  
operations={"+":add, "-":sub,"*":multiply,"/":divide,"**":expo,"r":root}
def calculator():
  print(logo)
  
  first_number=float(input("First Number: "))  
  for ope in operations.keys(): #or for ope in operatons: can be used
    print(ope)
  
  while True:
    ope_symbol=input("Pick one of the symbols above: ")
    ope_function=operations[ope_symbol]
    second_number=float(input("Second Number: "))
    answer=ope_function(first_number,second_number)
    print(f"{first_number} {ope_symbol} {second_number} = {answer}")
    ask=input(f"""Type 'y' to continue calculating with {answer},or 
    type 'n' to start a new calculation: """)
    if ask == "y":
      first_number=answer 
    elif ask=="n":
      calculator()
    else:
      print("Wrong input, read carefully!")
      break
calculator()
