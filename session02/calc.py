print(f"Daniel James Rodgers HW1 & HW2 \n")


# Session 1 HW
print(f"     HW1")

time = 42*60 + 42 # Compute the amount of seconds in 42 minutes and 42 seconds
print(f"There are {time} seconds in 42 minutes and 42 seconds")

distance = 10/1.61 # Compute how many miles in 10KM
print(f"There are {distance:.2f} miles in 10 kilometers")

speed = distance/(time/60**2) # Compute MPH for 10KM in 42 minutes and 42 seconds 
print(f"If you run 10km in 42 minutes and 42 seconds, your average speed is {speed:.2f} mph \n")


#Session 2 HW
print(f"     HW2")

pi = 3.1415926 # Define variable pi
volume = 4*pi*5**3/3 # Compute volume of sphere with radius 5
print(f"A sphere with radius 5 has a volume of {volume:.1f}")

copies = 60 # Books ordered
books_cost = 24.95*0.6*copies # Total cost of books with price $24.95 with 40% discount 
shipping_cost = 3 + 0.75*(copies - 1) # Total shipping cost of books with cost $3 for first copy, and 75c per additional book
print(f"Total wholesale cost for 60 copies, at a unit cost of $24.95 discounted 40%, and a shipping cost of $3 for the first book and $0.75 for additional books, is ${books_cost + shipping_cost:.2f}") # Calculate unit cost + shipping cost

# Could import a library, but below is modular arithmetic instead
start_time = 6*60 + 52 # Start time of 6:52 converted to minutes
time_1 = 1 * (8 + 15/60) # Time (minutes) of first stint of 1 mile at 8m15 per mile
time_2 = 3 * (7 + 12/60) # Time (minutes) of second stint of 3 miles at 7m12 per mile
time_3 = time_1 # Same as Time_1, Time (minutes) of third stint of 1 mile at 8m15 per mile
finish_time = start_time+time_1+time_2+time_3 # Finish time (minutes) after midnight
finish_hour = int((finish_time / 60) % 24) # Hours after midnight of finish time, modulo 24 keeps the time to a 24h clock  
finish_minute = int((start_time+time_1+time_2+time_3) % 60) # Minutes after the hour of finish time, time in minutes modulo 60
print(f"If I leave my house at 06:52 and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, I get home for breakfast at {finish_hour:02d}:{finish_minute:02d}")

rise = (89/82 - 1)*100 # Percent rise from 82 to 89
print(f"If my average grade rises from 82 to 89, the percentage increase is {rise:.1f}%")