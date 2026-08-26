a = int(input("enter first number:"))
b = int(input("enter the second number:"))
c = input("enter the opration(+,-,*,/,)")

match c:
    case "+":
        print("Than two number sum",a+b)
    case "-":
        print("Than Two number Sub...",a-b)
    case "*":
        print("Than Two number mult",a*b)
    case "/":
        print("Than Two number divi",a/b)
    case _:
        print("Your answer default:")