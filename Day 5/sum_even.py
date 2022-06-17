#calculate the sum of even numbers between 1 and 100
#ie 2+4+6+....+100.

total = 0;
for i in range (2,101,2):
    total += i;
print(total);