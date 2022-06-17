'''
For all numbers in range 1, 100 inclusive 
if number divisible by 3 then print Fizz
if number divisible by 5 then print Buzz
if number divisible by both 3 and 5 print FizzBuzz
'''
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz");
        continue;
    elif i%3 == 0:
        print("Fizz");
        continue;
    elif i%5 == 0:
        print("Buzz");
        continue;
    else:
        print(i);

    