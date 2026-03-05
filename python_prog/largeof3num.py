a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print("largest number:", a)
elif b>a and b>c:
    print("largest number:", b)
else:
    print("largest number:", c)