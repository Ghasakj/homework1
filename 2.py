#2
decimal=int(input('enter a decimal number'))
binary=[]
while True:
    binary.append(str(decimal%2))
    decimal//=2
    if decimal==0:
        break
binary.reverse()
print(''.join(binary))
