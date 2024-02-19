#Total distance in KMs
total_distance_km = 10

#Total time in mins and secs
total_time_minutes = 42
total_time_seconds = 42

total_time_minutes += total_time_seconds / 60
total_distance_miles = total_distance_km * 0.62

#average pace per mile
average_pace_per_mile_minutes = total_time_minutes / total_distance_miles
print(average_pace_per_mile_minutes)

#Converting average pace to minutes and seconds
average_pace_minutes = int(average_pace_per_mile_minutes)
average_pace_seconds = int((average_pace_per_mile_minutes - average_pace_minutes) * 60)

#average speed in miles per hour
average_speed_mph = total_distance_miles / (total_time_minutes / 60)

print(f"Average pace: {average_pace_minutes} minutes {average_pace_seconds} seconds per mile")
print(f"Average speed: {average_speed_mph:.2f} miles per hour")