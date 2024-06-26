def is_prime(number):
    # 1 is a not prime so if to selct less than 2
    if number < 2:
        return False
    #for i in range 2 to square root of the number 
    for i in range(2, int(number**0.5) + 1):
    #if the range number is divisable and remainder is zero returns true 
        if number % i == 0:
            return False
    return True

# Test the function

def get_prime(st,e):
    li=[]
    for i in range(st,e+1):
        if is_prime(i):
            li.append(i)
    return li

a=get_prime(0,100)
print(a)



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a list of prime numbers from 2 to 100 using list comprehension
prime_list = [x for x in range(2, 101) if is_prime(x)]
print(prime_list)



def is_prime(number):
    # 1 is a not prime so if to selct less than 2
    if number < 2:
        return False
    #for i in range 2 to square root of the number 
    for i in range(2, int(number**0.5) + 1):
    #if the range number is divisable and remainder is zero returns true 
        if number % i == 0:
            return False
    return True


a=[8,42,2,4,5,7,8,555,6,7,5,432,343,3,4,4,54,2,2]
b=[i for i in a if is_prime(i)]
print(b)

