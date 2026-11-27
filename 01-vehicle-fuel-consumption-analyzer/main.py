print("****Fuel Efficiency Calculator****")

distance = float(input("How far did you drive? Enter distance in KM: "))
fuel = float(input("How much fuel did you use? Enter fuel in Liters: "))
fuel_price = float(input("Enter fuel price per Liter: "))

if fuel == 0:
    print("No fuel was used. Cannot calculate fuel efficiency.")

elif distance <= 0:
    print("Distance must be greater than zero.")

else:
    km_per_liter = round(distance / fuel, 2)

    liters_per_100km = round((fuel / distance) * 100, 2)

    cost_per_km = round((fuel * fuel_price) / distance, 2)

    if km_per_liter >= 15:
        rating = "Efficient"

    elif km_per_liter >= 10:
        rating = "Average"

    else:
        rating = "High use"

    print("\n===== Fuel Efficiency Report =====")

    print(f"Distance: {distance} KM")
    print(f"Fuel Used: {fuel} Liters")
    print(f"Fuel Price: {fuel_price} Taka/Liter")

    print("------------------------------")

    print(f"Fuel Efficiency: {km_per_liter:.2f} KM/L")
    print(f"Fuel Consumption: {liters_per_100km:.2f} L/100KM")
    print(f"Cost per KM: {cost_per_km:.2f} Taka/km")
    print(f"Rating: {rating}") 


