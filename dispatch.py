import main
import dec_to_hex, divide, sin, factorial, inverse, ln, power, quotient, subtract, tan, absolute, multiply, root
def dispatch(s):
    resolve = s.split()
    operation = resolve[1]
    try:
        resolve[0] = int(resolve[0])
        resolve[2] = int(resolve[2])
    except:
        pass

    if operation == "+":
        return add.add(resolve[0], resolve[2])
    elif operation == "-":
        return minus.minus(resolve[0], resolve[2])
    elif operation == "*":
        return multiply.multiply(resolve[0], resolve[2])
    elif operation == "/":
        return divide.divide(resolve[0], resolve[2])
    elif operation == "!":
        return factorial.factorial(resolve[0])
    elif operation == "to_hex":
        return dec_to_hex.dec_to_hex(resolve[0])
    elif operation == "to_bin":
        pass
    elif operation == "inv":
        return inverse.inverse(resolve[0])
    elif operation == "**":
        return power.power(resolve[0], resolve[2])

