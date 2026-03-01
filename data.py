def get_student_grades():
    """Gets student grades from CVS File"""
    student_grades = []

    file = open("data.csv", "r")
    for line in file:
        clean = line.strip()
        student_grades.append(clean)
    file.close()

    return student_grades

