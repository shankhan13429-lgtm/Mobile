print("="*50)
print("WELCOME TO CAFFEE")
print("="*50)

menu={
    1:"coffee - ₹ 50",
    2:"Tea - ₹ 20",
    3:"Samosa - ₹ 40",
    4:"Green Tea - ₹ 50",
}


while True:
    print("1.coffee ........")
    print("2. Tea............")
    print("3. Samosa ........")
    print("4.Green Tea........")

    choice = int(input("enter the number:"))
    qyt =int(input("your Qyt:"))

    if (choice==1):
        print("Your order is Coffee - ₹ ",50*qyt)
    elif (choice ==2):
        print("Your Order is Tea - ₹ ",20*qyt)
    elif (choice==3):
        print("Your Order is Samosa - ₹",40*qyt)
    elif (choice==4):
        print("Your Order is Green Tea - ₹",50*qyt)
    else:
        print("Thanku sar:")