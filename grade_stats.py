import statistics


def calculate_summary_stats(student_grades):
    """ Calculates statistics that summarize all schools
    :param student_grades: CSV list of student grade information
    :return A tuple with the summary statistics """

    schools = []
    courses = []
    students = []

    index = 0
    while index < len(student_grades):
        student_data = student_grades[index].split(',')

        school = student_data[0]
        course = student_data[1]
        student = student_data[2]

        if school not in schools:
            schools.append(school)

        if course not in courses:
            courses.append(course)

        if student not in students:
            students.append(student)

        index += 1

    num_schools = len(schools)
    num_courses = len(courses)
    num_students = len(students)

    return num_schools, num_courses, num_students


def calculate_school_stats(school_name, student_grades):
    """ Calculates statistics that summarize all schools
    :param school_name: Name of the school for which to get the statistics
    :param student_grades: CSV list of student grade information
    :return A tuple with the summary statistics """

    grades = []
    courses = []
    students = []

    index = 0
    while index < len(student_grades):
        student_data = student_grades[index].split(',')

        if student_data[0] == school_name:
            grade = float(student_data[3])
            course = student_data[1]
            student = student_data[2]

            grades.append(grade)

            if course not in courses:
                courses.append(course)

            if student not in students:
                students.append(student)

        index += 1

    if len(grades) == 0:

        school_exists = False
        num_courses = 0
        num_students = 0
        average_grade = 0
        median_grade = 0
        min_grade = 0
        max_grade = 0
    else:
        school_exists = True
        num_courses = len(courses)
        num_students = len(students)
        average_grade = sum(grades) / len(grades)
        median_grade = statistics.median(grades)
        min_grade = min(grades)
        max_grade = max(grades)

    return school_exists, num_courses, num_students, average_grade, median_grade, min_grade, max_grade

