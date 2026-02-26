import datetime


def display_school_summary(num_schools, num_courses, num_students):
    """ Displays a summary of the student grade data
    :param num_schools: Number of unique schools in the data
    :param num_courses: Number of unique courses in the data
    :param num_students: Number of unique students in the data """

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Report:          {time}")
    print(f"Number Schools:  {num_schools}")
    print(f"Number Courses:  {num_courses}")
    print(f"Number Students: {num_students}")


def display_school_statistics(school_name, school_exists, num_courses, num_students,
                              average_grade, median_grade, lowest_grade, highest_grade):
    """ Displays the statistics for the specified student
    :param school_name: Name of the school for the report
    :param school_exists: Indicates if the school actually exists
    :param num_courses: Number of courses the school
    :param num_students: Number of students in the school
    :param average_grade: Average grade of the students in the school
    :param median_grade: Median grade of the students in the school
    :param lowest_grade: Lowest grade for the school
    :param highest_grade: Highest grade for the school """

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # If school does not exist
    if not school_exists:
        print(f"School {school_name} does NOT exist!")
        return

    # If school exist
    print(f"Report:          {time}")
    print(f"School:          {school_name}")
    print(f"Number Courses:  {num_courses}")
    print(f"Number Students: {num_students}")
    print(f"Average Grade:   {average_grade:.1f}%")
    print(f"Median Grade:    {median_grade:.1f}%")
    print(f"Lowest Grade:    {lowest_grade:.1f}%")
    print(f"Highest Grade:   {highest_grade:.1f}%")
