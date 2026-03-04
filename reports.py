import datetime


def display_school_summary(num_schools, schools, num_courses, num_students, school_avg, school_min, school_max):
    """ Displays a summary of the student grade data
    :param num_schools: Number of unique schools in the data
    :param schools: List the names of the schools
    :param num_courses: Number of unique courses in the data
    :param num_students: Number of unique students in the data
    :param school_avg: List the school names and the average grade
    :param school_min: List the school names and the lowest grade
    :param school_max: List the school names and the highest grade
    """

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Report:          {time}")
    print(f"Number Schools:  {num_schools}")
    print(f"Schools:         {','.join(schools)}")
    print()
    print(f"Number Courses:  {num_courses}")
    print(f"Number Students: {num_students}")

    print("School Averages:")
    for school in schools:
        print(f"             {school}: {school_avg:.1f}%")

    print("School Minimums:")
    for school in schools:
        print(f"             {school}: {school_min:.1f}%")

    print("School Maximums:")
    for school in schools:
        print(f"             {school}: {school_max:.1f}%")


def display_school_statistics(school_name, school_exists, num_courses, course, num_students,
                              average_grade, median_grade, top_student, top_grade, bottom_student, low_grade):
    """ Displays the statistics for the specified student
    :param school_name: Name of the school for the report
    :param school_exists: Indicates if the school actually exists
    :param num_courses: Number of courses the school
    :param course: Displays name of courses in the school
    :param num_students: Number of students in the school
    :param average_grade: Average grade of the students in the school
    :param median_grade: Median grade of the students in the school
    :param top_student: Displays top student in the school
    :param top_grade: Displays top grade in the school
    :param bottom_student: Displays bottom student in the school
    :param low_grade: Displays bottom grade in the school"""

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # If school does not exist
    if not school_exists:
        print(f"School {school_name} does NOT exist!")
        return

    # If school exist
    print(f"Report:          {time}")
    print(f"School:          {school_name}")
    print(f"Number Courses:  {num_courses}")
    print(f"Courses:         {','.join(course)}")
    print(f"Number Students: {num_students}")
    print(f"Average Grade:   {average_grade:.1f}%")
    print(f"Median Grade:    {median_grade:.1f}%")
    print(f"Top Student:     {top_student}")
    print(f"Top Grade:       {top_grade:.1f}%")
    print(f"Bottom Student:  {bottom_student}")
    print(f"Bottom Grade:    {low_grade:.1f}%")
