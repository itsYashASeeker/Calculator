from replit import clear
from art import logo
clear()
print(logo)

def add(n1, n2):
  return n1+n2

def sub(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def division(n1, n2):
  return n1/n2  

dict = {
  "+":add,
  "-":sub,
  "*":multiply,
  "/":division
}    
def calculator():
  num_other = float(input("What's the first number? "))
  end="yes"
  while end=="yes":
    for symbol in dict:
      print(symbol)
    operation_sym=input("Pick one operation! ")
    num2=float(input("What's the next number? "))
    function_call = dict[operation_sym]
    answer = function_call(num_other, num2)
    print(f"{num_other} {operation_sym} {num2} = {answer}")
    num_other = answer
    end = input("More Numbers? Type 'yes' for input! orelse 'no' to end -- ")
    if end=="no":
      print("--------------------")
      calculator()
    elif not end=="yes":
      print("Invalid input!") 
calculator()