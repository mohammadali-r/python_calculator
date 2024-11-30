from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import divide

num_1 = int(input("\033[33m ----- Enter your first number: -----\033[30m\n"))
num_2 = int(input("\033[33m ----- Enter your second number: -----\033[30m\n"))
op = input("\033[33m ----- Enter your operand: -----\033[30m\n")

def main(n1, n2, o):
    if n1 and n2 and o == "":
        print("\033[33m *** Please enter your numbers and operand ***\033[30m")
    else:
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
# TODO 2. R&D for usage return and print
# TODO 3. handle edge cases