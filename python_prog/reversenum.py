n = int(input())
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 +rem
    n = n // 10
print(rev)

n = int(input())
rev = int(str(n)[::-1])
print(rev)