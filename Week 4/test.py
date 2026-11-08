# cos 101 test

#input

count=0

for student_number in range (1,60):
    score = float(input("Score"))
    if score >= 50:
      count += 1
      print(f"{student_number}: {score}: You pass")
    else:
        count += 1
        print(f" {student_number}:{score}:You fail")
        
