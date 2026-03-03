def get_student_grades():
    """Gets student grades from CVS File"""
    fh = open("data.csv", "r")
    data = fh.readline()
    fh.close()

    student_grades = []

    for line in data:
        clean = line.strip(",")
        student_grades.append(clean)
    return student_grades
