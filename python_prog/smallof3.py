a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
if a<b and a<c:
    print("smallest number is:", a)
elif b<a and b<c:
    print("smallest number is:", b)
else:
    print("smallestnumber is:", c)