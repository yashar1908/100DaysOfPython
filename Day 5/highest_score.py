#output the highest score from a given list of scores
scores = [1,2,3,1,4,5,6,1,2,4,7,7,7,2,3,4,1,3,4,8,6,1,5,2,3,1];
max = 0;
for score in scores:
    if score > max:
        max = score;
print("The highest score is:",max);