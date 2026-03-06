def get_student_grades():
    """Gets student grades from CVS File"""
    student_grades = []

    fh = open("data.csv", "r")

    for line in fh:
        clean = line.strip()
        student_grades.append(clean)

    fh.close()

    return student_grades
