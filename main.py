###solution to problem 66 from ben stephenson's "the python workbook"

print("Enter a letter grade:")
grade = str(input()).upper()

grades = {  'F':   0,
            'D':   1,
            'D+':  1.3,
            'C-':  1.7,
            'C:':  2.0,
            'C+':  2.3,
            'B-':  2.7,
            'B':   3.0,
            'B+':  3.3,
            'A-':  3.7,
            'A':   4.0  }

grade_letters = grades.keys()
numerical_grades = []

while grade != '':
  for k in grade_letters:
    if grade == k:
      numerical_grades.append(grades[k])
  print("Enter a letter grade:")
  grade = str(input()).upper()

print(f'Your GPA is {sum(numerical_grades) / len(numerical_grades)}.')
