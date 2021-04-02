name=(input("enter a string"))
user=name.lower()

if user[::]==user[::-1]:
    print("it is a palindrome")
else:
    print("it is not")