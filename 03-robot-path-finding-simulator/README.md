# 🤖 P03 - Robot Grid Navigator

## 1. Project Summary

Robot Grid Navigator is a Python-based project where a robot moves inside a 5×5 grid using user commands.

The robot starts at position `(0, 0)` facing North. It can move forward, turn left, and turn right. The program also detects grid boundaries and handles unknown commands.

### Small Grid Picture

```text
       0    1    2    3    4
     +----+----+----+----+----+
  4  |    |    |    |    |    |
     +----+----+----+----+----+
  3  |    |    |    |    |    |
     +----+----+----+----+----+
  2  |    |    |    |    |    |
     +----+----+----+----+----+
  1  |    |    |    |    |    |
     +----+----+----+----+----+
  0  | 🤖 |    |    |    |    |
     +----+----+----+----+----+
```

*Starting Position: (0, 0) — Facing North*

## 2. Command List

The robot supports three basic commands:

| Command | Description |
|:---:|---|
| `F` | Move Forward one step |
| `L` | Turn Left |
| `R` | Turn Right |

Commands can be entered together as a sequence.

Example: `FFRF`

## 3. How to Run

**Requirements:** Python 3

Follow these steps:

1. Open the project folder.
2. Open the terminal in VS Code.
3. Run the following command:

```bash
python main.py
```

4. Enter the robot commands when prompted.

## 4. Sample Commands and Output

### Example 1: Normal Movement

**Input:**
```text
FFRF
```

**Output:**
```text
Final Result
Final Position: (1, 2)
Final Direction: East
```

### Example 2: Boundary Detection

**Input:**
```text
FFFFFF
```

**Output:**
```text
Warning: Grid boundary reached!
Warning: Grid boundary reached!

Final Result
Final Position: (0, 4)
Final Direction: North
```

### Example 3: Invalid Command

**Input:**
```text
FXR
```

**Output:**
```text
Warning: Unknown command: X

Final Result
Final Position: (0, 1)
Final Direction: East
```

## 5. What I Learned

Through this project, I learned:

- Python functions and modules.
- Loops and conditional statements.
- Working with lists and coordinates.
- Robot movement and direction control.
- Grid boundary checking.
- Handling unknown commands.
- Testing and debugging Python programs.

## 6. Next Idea: Obstacles

In the future, I would like to improve this project by adding obstacles inside the grid.

The robot will need to detect obstacles and avoid moving into blocked cells.

---

**Project Name:** P03 - Robot Grid Navigator  
**Programming Language:** Python  
**Project Type:** Grid-Based Navigation