# Test Cases – Robot Grid Navigator

This file contains the test cases used to verify the Robot Grid Navigator project. Each test checks robot movement, direction changes, grid boundaries, and invalid commands.

## Test Case Summary

| Test No. | Input Commands | Expected Final Position | Expected Direction | Expected Warnings | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `FFRF` | `(1, 2)` | East | 0 | Passed |
| 2 | `FFFFFF` | `(0, 4)` | North | 2 | Passed |
| 3 | `LLFF` | `(0, 0)` | South | 2 | Passed |
| 4 | `FXR` | `(0, 1)` | East | 1 (Unknown command) | Passed |

## Detailed Test Results

### Test Case 1: Normal Movement and Turning

- **Input:** `FFRF`
- **Expected Position:** `(1, 2)`
- **Expected Direction:** East
- **Warnings:** None

| Command | Position | Direction |
|:---:|:---:|:---:|
| F | `(0, 1)` | North |
| F | `(0, 2)` | North |
| R | `(0, 2)` | East |
| F | `(1, 2)` | East |

**Result:** Passed

### Test Case 2: Grid Boundary Checking

- **Input:** `FFFFFF`
- **Expected Position:** `(0, 4)`
- **Expected Direction:** North
- **Expected Warnings:** 2 boundary warnings

| Command | Position | Direction | Warning |
|:---:|:---:|:---:|:---|
| F | `(0, 1)` | North | None |
| F | `(0, 2)` | North | None |
| F | `(0, 3)` | North | None |
| F | `(0, 4)` | North | None |
| F | `(0, 4)` | North | Grid boundary reached! |
| F | `(0, 4)` | North | Grid boundary reached! |

**Result:** Passed

### Test Case 3: Left Turns and Boundary Checking

- **Input:** `LLFF`
- **Expected Position:** `(0, 0)`
- **Expected Direction:** South
- **Expected Warnings:** 2 boundary warnings

| Command | Position | Direction | Warning |
|:---:|:---:|:---:|:---|
| L | `(0, 0)` | West | None |
| L | `(0, 0)` | South | None |
| F | `(0, 0)` | South | Grid boundary reached! |
| F | `(0, 0)` | South | Grid boundary reached! |

**Result:** Passed

### Test Case 4: Invalid Command Handling

- **Input:** `FXR`
- **Expected Position:** `(0, 1)`
- **Expected Direction:** East
- **Expected Warning:** Unknown command: X

| Command | Position | Direction | Warning |
|:---:|:---:|:---:|:---|
| F | `(0, 1)` | North | None |
| X | `(0, 1)` | North | Unknown command: X |
| R | `(0, 1)` | East | None |

**Result:** Passed

## Conclusion

All four test cases were executed successfully. The robot correctly handles forward movement, left and right turns, grid boundary restrictions, and unknown commands.

The actual outputs matched the expected results in all test cases.