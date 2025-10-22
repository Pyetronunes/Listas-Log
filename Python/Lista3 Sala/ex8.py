a, b = 1, 1
print(a, b, end=" ")

for i in range(3, 16):
    c=a+b
    print(c, end=" ")
    a=b
    b=c