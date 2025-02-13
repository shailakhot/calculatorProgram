import art

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))
    while should_continue:
      for symbol in operations:
        print(symbol)

      operator = input("Pick an operation: ")
      num2 = float(input("What's the first number?: "))
      result = operations[operator](num1, num2)
      print(f"The result is {num1} {operator} {num2} = {result}")
      choice = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
      if choice == "y":
        num1 = result
      elif choice == "n":
       should_continue = False
       print("\n"*20)
       calculator()


calculator()