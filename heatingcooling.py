# Utility company would like to have an estimate of energy requirements for a few days. If (average) temperature during a day is below 60 degrees Farenheit, 
# that day is considered to be a heating day (people are very likely to run a heater in their houses on such day). 
# If the temperature is above 80F, this day is considered a cooling day (people are very likely to turn on A/C on such day). 
# Write a program that asks the user
# ```
# Enter the average daily temperature:
# ```
# and calculates the running totals of heating and cooling days. The program should print these two totals after all the data has been processed.
# Assume that input and output types are integers. End of input is denoted by user entering a value lower than -459 (the lowest possible temperature).

# Sample run:
# ```
# Enter the average daily temperature: 33
# Enter the average daily temperature: 90
# Enter the average daily temperature: 98
# Enter the average daily temperature: 66
# Enter the average daily temperature: 22
# Enter the average daily temperature: -460
# Heating days: 2
# Cooling days: 2
# ```
# Thoroughly test your program. 

temp = 0
cool = 0
heat = 0
while True:
    temp = int(input("Enter the average daily temperature: "))
    if temp < -459:
        break
    elif temp < 60:
        heat += 1
    elif temp > 80:
        cool += 1

print('Heating days: ', heat)
print('Cooling days: ', cool)