n=int(input('Enter n: '))
for i in range(n-1):
    k=ord("A")
    for j in range(i,n):
        print(end=" ")
    for j in range(i):
        print(chr(k), end=" ")
        k+=1
    for j in range(1):
        print(chr(k), end=" ")
        k+=1
    print()
for i in range(n):
    k=ord("A")
    for j in range(i+1):
        print(end=" ")
    for j in range(n-i):
        print(chr(k), end=" ")
        k+=1
    print()