from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import divide

num_1 = int(input("Enter your first number: \n"))
num_2 = int(input("Enter your second number: \n"))
op = input("Enter your operand: \n")

def main(n1, n2, o):
    if n1 and n2 and o == "":
        print("Please enter your numbers and operand")
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
print(res)