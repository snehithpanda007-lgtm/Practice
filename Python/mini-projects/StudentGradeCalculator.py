coding = int(input("Enter Coding marks: "))
english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))

Pass = coding >= 60 and english >= 60 and maths >= 60
total = coding + english + maths
average = total/3
if Pass and average == 100:
    grade = "S"
elif Pass and average >= 90:
    grade = "A"
elif Pass and average >= 80:
    grade = "B"
elif Pass and average >= 70:
    grade = "C"
elif Pass and average >= 60:
    grade = "D"  
else:
    grade = "F"  
    
print("Grade: ", grade)
print("Average: ", str(average))
print("Total: ", str(total))