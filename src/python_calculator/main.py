from utils.add import add
from utils.subtract import subtract
from utils.multiply import multiply
from utils.divide import divide

try:
    num_1 = int(input("\033[33m ----- Enter your first number: -----\033[30m\n"))
except ValueError:
    raise SystemExit("\033[33m *** Please enter your numbers ***\033[30m")

try:
    num_2 = int(input("\033[33m ----- Enter your second number: -----\033[30m\n"))
except ValueError:
    raise SystemExit("\033[33m *** Please enter your numbers ***\033[30m")

op = input("\033[33m ----- Enter your operand: -----\033[30m\n")

if op == "":
    raise SystemExit("\033[33m *** Please enter your operation ***\033[30m")
else:

    def main(n1, n2, o):
        match o:
            case "+":
                return add(n1, n2)
            case "-":
                return subtract(n1, n2)
            case "*":
                return multiply(n1, n2)
            case "/":
                return divide(n1, n2)
            case _:
                return "Invalid operation"


res = main(num_1, num_2, op)
print("\033[32m ----- RESULT ----- \n\033[1m" + str(res) + "\033[30m\033[0m")
