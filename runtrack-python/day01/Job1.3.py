#Job 1.3
def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 40:
            rounded_grades.append(grade)
        if grade >40:
            next_multiple_of_5 = ((grade + 4) // 5) * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    return rounded_grades

# Exemple:
grades = [87, 82, 75, 37, 94,41]
rounded_grades = round_grades(grades)
print(rounded_grades)
