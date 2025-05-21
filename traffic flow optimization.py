# Average cars per minute from each direction
traffic = {
    'North': 30,
    'South': 20,
    'East': 50,
    'West': 40
}

# Total green light time per cycle (in seconds)
total_time = 120

# Total traffic
total_cars = sum(traffic.values())

# Calculate green time per direction (proportional to traffic)
green_times = {
    direction: (cars / total_cars) * total_time
    for direction, cars in traffic.items()
}

# Display results
print("Green light times (in seconds):")
for direction, time in green_times.items():
    print(f"{direction}: {time:.1f} seconds")
