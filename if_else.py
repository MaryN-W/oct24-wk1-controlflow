is_raining = False # Boolean

# if is_raining == False: # Colon starts a block. == True is redundant as is_raining is already a Boolean value. We could just say if is_raining:
#  print('I need an umbrella!') # Indents automatically
# else:
#  print('No need for an umbrella')

#  print('The end!!') # Outdent to escape block

# Ternary # A compact way to write a simple conditional (if-else) statement
# print('I need an umbrella!') if is_raining else print ('No need for an umbrella')
print('I need an umbrella!' if is_raining else 'No need for an umbrella')
# Else if

# >=80 -> HD
# 70-79 -> D
# 60-69 -> C
# 50-59 -> P
# <50 -> F

# marks = 44

# if marks >= 80:
#     print('HD')
# elif marks >= 70: # and marks < 80: # Contraction of else if
#     print ('D')
# elif marks >= 60:
#     print('C')
# elif marks >= 50:
#     print('P')
# else: 
#     print('F')

# Nested if

# 2 states -> State1 abd State2
# State1: >=18 can vote
# State2: >=21 can vote

# state = 'State2'
# age = 19 # age is a variable

# # Display whether they can vote or not
# # if (state == 'State1' and age >= 18) or (state == 'State2' and age >= 21)
# if state == 'State1':
#     if age >= 18:
#         print('Can vote in State 1')
#     else:
#         print('Cannot vote in State 1')
# else:
#     if age >= 21:
#         print('Can vote in State 2')
#     else:
#         print('Cannot vote in State 2')

# day_of_week = 7

# if day_of_week == 1:
#     print('Monday')
# elif day_of_week == 2:
#     print('Tuesday')

# match day_of_week:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5:
#         print('Friday')

#     case _: # Wildcard - Matches any value if none of the above # Last
#         print('That is not a weekday!')

# # 1-5: Weekday
# # 6-7: Weekend
# # Anything else : Error messsage
# match day_of_week:
#     case 1 | 2 | 3 | 4 | 5: # Instead of repeating above multiple times
#         print('Weekday')
#     case 6 | 7:
#         print('Weekend')
#     case _:
#         print('Error: Not a valid day number')

