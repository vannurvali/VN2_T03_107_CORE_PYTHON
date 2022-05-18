



#print prime numbers
for num in range(1,1000,1):
    if num > 1:
        for i in range (2,num):
            if (num%i) == 0:
                break
        else:
            print(num, end=' ')

#2.method
number = int(input('enter any number :'))
if number > 1:
    for i in range (2,number):
        if (number%i )== 0:
            print(number,'is not prime number')
            break
    else:
            print(number,'is prime number')