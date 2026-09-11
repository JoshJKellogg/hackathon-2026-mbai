# Josh Jeon and CJ (Christopher) Priedel
# Write a program that is given two integers representing a speed limit and driving speed in miles per hour (mph) and outputs the traffic ticket amount.
# Driving 10 mph *under* the speed limit (or slower) receives a  \$50 ticket. Driving 6 - 20 mph *over* the speed limit receives a \$75 ticket.
# Driving 21 - 40 mph *over* the speed limit receives a \$150 ticket. Driving faster than 40 mph over the speed limit receives a \$300 ticket. Otherwise, no ticket is received
# Ex: If the input is:
# ```
# 35
# 45
# ```
# the output is:
# ```
# 75
# ```
# Ex: If the input is:
# ```
# 35
# 26
# ```
# the output is:
# ```
# 0
# ```
# *Note: there are no prompts displayed by input() function.*

# Thoroughly test your program. 

l = int(input())
s = int(input())
dif = s-l
if dif <= -10:
    print(50)
elif 6 <= dif <= 20:
    print(75)
elif 21 <= dif <= 40:
    print(150)
elif dif > 40:
    print(300)
