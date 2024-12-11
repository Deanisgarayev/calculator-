def calulator(a=int(input()), sign=str(input()), b=int(input())):
    if sign=="+":
        print(a+b)
    elif sign=="-":
        print(a-b)
    elif sign=="*":
        print(a*b)
    elif sign=="/":
        print(a/b)
    else:
        print("can not do this try another sign")
try:
    calulator()
except ZeroDivisionError:
    print("you are not allowed divide by zero")




