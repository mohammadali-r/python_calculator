from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import divide

try:
    num_1 = int(input("\033[33m ----- Enter your first number: -----\033[30m\n"))
except ValueError:
    print("\033[33m *** Please enter your numbers ***\033[30m")
    num_1 = ""
    
try:
    num_2 = int(input("\033[33m ----- Enter your second number: -----\033[30m\n"))
except ValueError:
    print("\033[33m *** Please enter your numbers ***\033[30m")
    num_2 = ""

op = input("\033[33m ----- Enter your operand: -----\033[30m\n")

def main(n1, n2, o):
    match o:
        case "+":
            return(add(n1, n2))
        case "-":
            return(subtract(n1, n2))
        case "*":
            return(multiply(n1, n2))
        case "/":
            return(divide(n1, n2))
        case _:
            return("Invalid operation")
                
res = main(num_1, num_2, op)
print("\033[32m ----- RESULT ----- \n\033[1m" + str(res) + "\033[30m\033[0m")


# TODO 1. fix git ignore

# TODO 3. handle edge cases

# test