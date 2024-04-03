digit = int(input('Enter integer: '))

number9 = digit % 10
number3 = (digit // 10) % 10
number2 = (digit // 10)//10 
num33 = number2 % 10
num22 = (number2 // 10) % 10
num44 = ((number2 // 10) // 10) % 10



print (num44, num22, num33, number3, number9)