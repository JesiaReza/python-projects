
# Fuel Efficiency Calculator

A simple Python program that calculates vehicle fuel efficiency and fuel cost per kilometer.

## Features

- Takes distance, fuel used, and fuel price as input.
- Calculates fuel efficiency in KM/L.
- Calculates fuel consumption in L/100KM.
- Calculates fuel cost per KM.
- Shows fuel efficiency rating.
- Displays a friendly message when fuel used is zero.

## Technologies Used

- Python
- Visual Studio Code (VS Code)

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

## Sample Input

```text
Distance: 450
Fuel Used: 30
Fuel Price: 120
```

## Sample Output

```text
===== Fuel Efficiency Report =====
Distance: 450.0 KM
Fuel Used: 30.0 Liters
Fuel Price: 120.0 Taka/Liter
------------------------------
Fuel Efficiency: 15.00 KM/L
Fuel Consumption: 6.67 L/100KM
Cost per KM: 8.00 Taka/km
Rating: Efficient
```

## What I Learned

- Taking user input using input().
- Converting input using float().
- Using arithmetic operators.
- Using round() for decimal values.
- Applying if, elif, and else conditions.
- Formatting output using f-strings.
- Testing a Python program.

## Future Improvements

- Add more detailed input validation.
- Allow users to calculate fuel costs for multiple trips.
- Save calculation history.
