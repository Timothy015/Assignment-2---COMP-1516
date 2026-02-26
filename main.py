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

        num_schools, num_courses, num_students = grade_stats.calculate_summary_stats(student_grades)
        reports.display_school_summary(num_schools, num_courses, num_students)

    # School Report
    elif report_type == "school":
        if len(sys.argv) != 3:
            print("Not enough arguments for the School Report.")
            sys.exit(0)

        school_name = sys.argv[2]
        (school_exists, num_courses, num_students, average_grade, median_grade,
            min_grade, max_grade) = grade_stats.calculate_school_stats(school_name, student_grades)

        reports.display_school_statistics(school_name, school_exists, num_courses, num_students,
                                          average_grade, median_grade, min_grade, max_grade)

    # Invalid report type
    else:
        print("Invalid report type. Must be summary or school.")
        sys.exit(0)


if __name__ == "__main__":
    main()
