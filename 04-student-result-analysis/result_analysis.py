def calculate_average(marks):
    total_marks = 0
    if len(marks)==0:
        return "No marks available"
    else:
        for mark in marks:
            total_marks += mark

        average = total_marks/len(marks)
        return round(average,2)

def find_highest(marks):
    if len(marks) == 0:
        return "No marks available"
    else:
        return max(marks)

def find_lowest(marks):
    if len(marks) == 0:
        return "No marks available"
    
    else:
        return min(marks)

def calculate_grade(marks):
    if marks>=80:
        return "A"

    elif marks>=70:
        return "B"

    elif marks>=60:
        return "C"

    elif marks>=40:
        return "D"
    
    else:
        return "F"

def count_passes(marks):
    passed = 0
    failed = 0
    for mark in marks:
        if mark>=40:
             passed += 1

        else:
            failed += 1

    return passed,failed

def calculate_pass_rate(passed,total_students):
    if total_students == 0:
        return 0

    else:
        pass_rate = (passed/total_students)*100
        return round(pass_rate,2)
            
        




