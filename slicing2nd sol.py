l1=[1,2,3,4,5]
index=int(input("Enter index value"))
element=(input("Enter a element"))
list1=l1[:index]+[element]+l1[index:]

print(list1)