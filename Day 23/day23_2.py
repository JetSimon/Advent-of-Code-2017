def isprime(n):
    for m in range(2,n):
        if n % m == 0:
            return False
    return True

b = 67
c = b
b *= 100
b -= -100000
c = b
c -= -17000

print(b,c)

h = 0

for n in range(b,c+17,17):
    if not isprime(n):
        h+=1

print(h)