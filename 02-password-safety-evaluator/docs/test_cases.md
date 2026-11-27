# Password Strength Checker – Test Cases

This file contains test cases used to check whether the Password Strength Checker works correctly.

| Test Case | Input | Expected Score | Expected Strength | Expected Result |
|---|---|---:|---|---|
| TC-01 | `abc` | 1/5 | Weak | Only lowercase condition is satisfied. |
| TC-02 | `Password1` | 4/5 | Medium | Special character is missing. |
| TC-03 | `Dhaka2026!` | 5/5 | Strong | All five conditions are satisfied. |
| TC-04 | Empty input | — | — | Ask for the password again without crashing. |

## Test Case Details

### TC-01: Weak Password

**Input:** `abc`

**Expected Output:**
```text
'abc' → 1/5 Weak
Use at least 8 characters.
Add an uppercase letter.
Add a number.
Add a special character.
```

### TC-02: Medium Password

**Input:** `Password1`

**Expected Output:**
```text
'Password1' → 4/5 Medium
Add a special character.
```

### TC-03: Strong Password

**Input:** `Dhaka2026!`

**Expected Output:**
```text
'Dhaka2026!' → 5/5 Strong
```

### TC-04: Empty Input

**Input:** Press Enter without typing anything.

**Expected Result:**
```text
Enter the password:
Password cannot be empty.
Enter the password:
```

The program should ask again and continue running without crashing.

## Testing Safety

Only fake passwords were used during testing. Real passwords should never be entered into this project.