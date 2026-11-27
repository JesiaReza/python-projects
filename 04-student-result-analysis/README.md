# Student Result Analysis

## Project Summary

Student Result Analysis is a beginner-friendly Python project that analyzes students' marks and generates a result report.

It calculates average marks, highest marks, lowest marks, individual grades, pass count, fail count, and pass rate.

### Grade Scale

| Marks | Grade |
|---|---|
| 80–100 | A |
| 70–79 | B |
| 60–69 | C |
| 40–59 | D |
| Below 40 | F |

## Features

- Take marks as user input.
- Validate marks between 0 and 100.
- Calculate average marks.
- Find highest and lowest marks.
- Calculate individual student grades.
- Count passed and failed students.
- Calculate pass rate.
- Display a final result report.
- Handle empty student lists.

## Technologies Used

- Python
- VS Code

## Project Structure

```text
04-student-result-analysis/
│
├── main.py
├── result_analysis.py
├── README.md
├── .gitignore
│
└── docs/
    └── test_cases.md
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python main.py
```

## Sample Marks and Report

**Input Marks:** `[72, 85, 38, 91, 64]`

**Expected Report:**

```text
Average Marks: 70.0
Highest Marks: 91
Lowest Marks: 38
Passed Students: 4
Failed Students: 1
Pass Rate: 80.0%
```

## What I Learned

- Python functions
- Lists and loops
- Conditional statements
- User input and input validation
- Return values
- Importing functions from another Python file
- Basic Git and GitHub workflow

## Future Improvements

- Add a menu-driven system.
- Store student results in a file.
- Add student names and IDs.
- Generate a detailed result sheet.