KM = 10
tot_miles = KM/1.61
min = 42
sec = 42
tot_mins = min  + sec / 60

average_pace_per_mile_mins = tot_mins / tot_miles
average_pace_mins = int(average_pace_per_mile_mins)
average_pace_secs = int((average_pace_per_mile_mins - average_pace_mins) * 60)

average_speed_mph = tot_miles / (tot_mins / 60)

print(f"Average pace: {average_pace_mins} mins {average_pace_secs} secs")
print(f"Average speed: {average_speed_mph:.2f} mph")

# The following is the Output
# Average pace: 6 mins 52 secs
# Average speed: 8.73 mph