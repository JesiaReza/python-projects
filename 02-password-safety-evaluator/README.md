# Password Strength Checker

## 1. Project Summary

Password Strength Checker is a beginner-friendly Python project that checks the strength of a password using five different rules. It calculates a score out of 5 and shows whether the password is Weak, Medium, or Strong.

It also provides suggestions to improve the password if any criteria are missing.

## 2. Password Scoring Rules

Each satisfied condition adds 1 point.

| Rule | Score |
|---|---:|
| At least 8 characters | 1 |
| Contains an uppercase letter | 1 |
| Contains a lowercase letter | 1 |
| Contains a number | 1 |
| Contains a special character | 1 |
| **Total** | **5** |

### Password Strength Levels

| Score | Strength |
|---|---|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

## 3. Features

- Checks password length.
- Detects uppercase and lowercase letters.
- Detects numbers and special characters.
- Calculates password strength out of 5.
- Gives suggestions for missing criteria.
- Allows users to check multiple passwords.
- Handles empty input without crashing.

## 4. Technologies Used

- Python

## 5. Python Concepts Used

- Strings
- `len()`
- `for` loop
- `while` loop
- `if`, `elif`, `else`
- `in` operator
- Boolean variables
- String methods: `isupper()`, `islower()`, `isdigit()`, `isalnum()`, `isspace()`
- `strip()`

## 6. How to Run

1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

```bash
python main.py
```

## 7. Sample Runs

### Example 1: Weak Password

```text
Enter the password: abc
'abc' → 1/5 Weak

Use at least 8 characters.
Add an uppercase letter.
Add a number.
Add a special character.
```

### Example 2: Medium Password

```text
Enter the password: Password1
'Password1' → 4/5 Medium

Add a special character.
```

### Example 3: Strong Password

```text
Enter the password: Dhaka2026!
'Dhaka2026!' → 5/5 Strong
```

### Example 4: Empty Input

```text
Enter the password:
Password cannot be empty.
Enter the password:
```

## 8. Safety Note

This project is for educational purposes only. Always use fake passwords for testing. Never enter your real passwords into this program.

## 9. What I Learned

Through this project, I learned how to use Python strings, loops, conditional statements, Boolean variables, and string methods to build a simple password strength checker.

## 10. Future Improvements

- Add more password validation rules.
- Improve the output format.
- Add a graphical user interface (GUI).