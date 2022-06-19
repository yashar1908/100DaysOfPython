def check_prime(num):
    factors = 0;
    for i in range(2,num):
        if(num%i==0):
            factors+=1;
    if(factors == 0):
        print(num,"is a prime number.");
    else:
        print(num,"is not a prime number.");

check_prime(7);
check_prime(13);
check_prime(12);