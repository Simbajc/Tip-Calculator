from art import logo

#Calculator
math_symbols = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multipy
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  end_of_calculation = False
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  
  while end_of_calculation is False:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
  
    if input(f"Type 'y' to continue calculationg with {answer},  or type 'n' to start a new calculation.: ") == 'y':
      num1 = answer
    else:
      end_of_calculation = True
      calculator()

calculator()