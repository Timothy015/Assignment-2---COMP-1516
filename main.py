import sys
import data
import grade_stats
import reports


def main():
    # Check arguments
    if len(sys.argv) < 2:
        print("Invalid number of arguments.")
        sys.exit(0)

    report_type = sys.argv[1]
    student_grades = data.get_student_grades()

    # Summary Report
    if report_type == "summary":
        if len(sys.argv) != 2:
            print("Invalid number of arguments.")
            sys.exit(0)

        num_schools, schools, num_courses, num_students, school_avg, school_min, school_max = (
            grade_stats.calculate_summary_stats(student_grades))

        reports.display_school_summary(num_schools, schools, num_courses, num_students,
                                       school_avg, school_min, school_max)

        # Prints summary into text file
        fh = open("summary.txt", "w")
        fh.write("Summary report generated\n")
        fh.write(f"Number Schools: {num_schools}\n")
        fh.write(f"Schools: {','.join(sorted(schools))}\n")
        fh.write(f"Number Courses: {num_courses}\n")
        fh.write(f"Number Students: {num_students}\n")
        fh.write("School Averages:\n")
        for school in schools:
            fh.write(f"             {school}: {school_avg[school]:.1f}%\n")

        fh.write("School Minimums:\n")
        for school in schools:
            fh.write(f"             {school}: {school_min[school]:.1f}%\n")

        fh.write("School Maximums:\n")
        for school in schools:
            fh.write(f"             {school}: {school_max[school]:.1f}%\n")
        fh.close()

    # School Report
    elif report_type == "school":
        if len(sys.argv) != 3:
            print("Not enough arguments for the School Report.")
            sys.exit(0)

        school_name = sys.argv[2]
        (school_name, school_exists, num_courses, courses, num_students,
         average_grade, median_grade, top_student, highest_grade, bottom_student, lowest_grade) = \
            (grade_stats.calculate_school_stats(school_name, student_grades))

        reports.display_school_statistics(school_name, school_exists, num_courses, courses, num_students,
                                          average_grade, median_grade, top_student, highest_grade, bottom_student,
                                          lowest_grade)

        # Prints report of requested school into text file
        file_name = school_name.lower() + ".txt"
        fh = open(file_name, "w")
        fh.write("School report generated\n")
        fh.write(f"School:          {school_name}\n")
        fh.write(f"Number Courses:  {num_courses}\n")
        fh.write(f"Courses:         {','.join(sorted(courses))}\n")
        fh.write(f"Number Students: {num_students}\n")
        fh.write(f"Average Grade:   {average_grade:.1f}%\n")
        fh.write(f"Median Grade:    {median_grade:.1f}%\n")
        fh.write(f"Top Student:     {top_student}\n")
        fh.write(f"Top Grade:       {highest_grade:.1f}%\n")
        fh.write(f"Bottom Student:  {bottom_student}\n")
        fh.write(f"Bottom Grade:    {lowest_grade:.1f}%\n")
        fh.close()

    # Invalid report type
    else:
        print("Invalid report type. Must be summary or school.")
        sys.exit(0)


if __name__ == "__main__":
    main()
