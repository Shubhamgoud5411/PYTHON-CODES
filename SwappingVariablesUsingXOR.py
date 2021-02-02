# Swapping Variables using XOR 
a = 5
b = 6

a = a ^ b # ^ = XOR
b = a ^ b
a = a ^ b

print(a)
print(b)