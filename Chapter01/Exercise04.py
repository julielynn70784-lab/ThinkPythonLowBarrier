"""
Chapter 1 - Exercise 04
Running a 10 km race in 42 minutes 42 seconds.
"""
KM_PER_MILE = 1.61

race_minutes = 42
race_seconds = 42
race_km = 10

# 1. How many seconds are there in 42 minutes 42 seconds?
total_seconds = race_minutes * 60 + race_seconds

# 2. How many miles are there in 10 kilometers?
race_miles = race_km / KM_PER_MILE

# 3. Average pace in seconds per mile
seconds_per_mile = total_seconds / race_miles

# 4. Average pace in minutes AND seconds per mile
#    divmod gives the whole minutes and the leftover seconds in one step
pace_minutes, pace_seconds = divmod(seconds_per_mile, 60)

# 5. Average speed in miles per hour
total_hours = total_seconds / 3600
miles_per_hour = race_miles / total_hours

print(f"1. {total_seconds} seconds in 42 minutes 42 seconds")
print(f"2. {race_miles:.2f} miles in {race_km} km")
print(f"3. {seconds_per_mile:.2f} seconds per mile")
print(f"4. {int(pace_minutes)} minutes {pace_seconds:.1f} seconds per mile")
print(f"5. {miles_per_hour:.2f} miles per hour")
