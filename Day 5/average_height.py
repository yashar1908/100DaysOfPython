#calculate the average height from a list of given heights 
heights = [102,109,140,156,164,170,189,176,180,200,139,123,159];
sum = 0;
for height in heights:
    sum += height;
average = sum/len(heights);
print("The average height is:",average);