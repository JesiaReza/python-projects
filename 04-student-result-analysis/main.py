from result_analysis import calculate_average,find_highest,find_lowest,calculate_grade,count_passes,calculate_pass_rate

marks = []

print("===== Student Result Analysis =====")

total_students = int(input("Enter number of students: "))

if total_students <= 0:
    print("No students available.")

else:
    for i in range(total_students):
        mark = int(input(f"Enter marks for student {i + 1}: "))

        while mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            mark = int(input(f"Enter marks for student {i + 1}: "))

        marks.append(mark)

    print("\n===== Student Results =====")

    for i in range(len(marks)):
        grade = calculate_grade(marks[i])
        print(f"Student {i + 1}: Marks = {marks[i]}, Grade = {grade}")

    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)

    passed, failed = count_passes(marks)

    pass_rate = calculate_pass_rate(passed, total_students)

    print("\n===== Final Report =====")
    print(f"Average Marks: {average}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")
    print(f"Pass Rate: {pass_rate}%")
