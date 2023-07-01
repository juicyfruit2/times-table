
# made use of for loops in order to display the times tables for any number.

# ask user to enter any nuber 
user_input = int(input("enter any numer:"))

# used the f string function 
print(f" the time table for {user_input } is:")

# used loop function as well as f strings to get time tables 
for i in range (1,13):
    print (f"{i} * {user_input} = {i * user_input}")