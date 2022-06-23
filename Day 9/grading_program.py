#You have the following dictionary containing student names and their scores:
student_scores = {
    "Harry": 81,
    "Ron": 78, 
    "Hermoine": 99, 
    "Draco": 74,
    "Neville": 62,
};

'''Write a program that converts scores to grades. By the end of your program you should have a new
dictionary called student_grades which has student names as keys and grades as values.
Grades are calculated as follows:
91-100: Outstanding
81-90: Exceeds Expectations
71-80: Acceptable
<=70: Fail
'''

student_grades = {};

for key in student_scores:
    score = student_scores[key];
    if score > 90:
        grade = "Outstanding";
    elif score > 80 and score <= 90:
        grade = "Exceeds Expectations";
    elif score > 70 and score <=80:
        grade = "Acceptable";
    else:
        grade = "Fail";
    student_grades[key] = grade;
    
print(student_grades);