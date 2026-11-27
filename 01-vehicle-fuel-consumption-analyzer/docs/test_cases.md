
# Fuel Efficiency Calculator - Test Cases

This document contains the test cases used to verify the Fuel Efficiency Calculator.

| Test Case | Distance (KM) | Fuel Used (L) | Fuel Price (Taka/L) | Expected Result | Actual Result | Status |
|---|---:|---:|---:|---|---|---|
| TC-01 | 450 | 30 | 120 | 15.0 KM/L, 6.67 L/100KM, 8.00 Taka/km, Efficient | 15.00 KM/L, 6.67 L/100KM, 8.00 Taka/km, Efficient | Pass |
| TC-02 | 100 | 10 | 120 | 10.0 KM/L, 10.00 L/100KM, 12.00 Taka/km, Average | 10.00 KM/L, 10.00 L/100KM, 12.00 Taka/km, Average | Pass |
| TC-03 | 100 | 0 | 120 | Friendly message without crashing | No fuel was used. Cannot calculate fuel efficiency. | Pass |
