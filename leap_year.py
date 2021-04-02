year = int(input("Enter year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("it is not  leap year")
    else:
        print("it is not  leap year")
    print("it is a leap year")
else:
    print("it is not  leap year")
