# Josh Jeon and CJ (Christopher) Priedel

# Write a function ```countchars(st)``` that take a string as a parameter and returns the number of characters in this string excluding spaces, periods, exclamation points, or commas.

# Ex: If the arugment is:
# ```
# Listen, Mr. Jones, calm down.
# ```
# the return value is:
# ```
# 21
# ```

# *Note: Account for all characters that aren't spaces, periods, exclamation points, or commas (Ex: "r", "2", "?").*

# * Write a program that asks the user for input string, calls your function on that input, and displays the returned value.

# * Using examples from Homework 5, add testing statements to your code. Make sure you have at least 5 tests that test different scenarios, and tests are both from black-box and clear-box categories. 

def countcharts(st):
    return len(st.replace(' ','').replace('.','').replace('!','').replace(',',''))

print(countcharts("a b c d e ,.!"))
assert countcharts("                   ") == 0
assert countcharts("this is a test !") == 11
