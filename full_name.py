#Beginner control structures task 1 - 
#Creating a program using if,elif,else and the boolean data type.
#The below Task will ask the user to input their full name.
# I have added a loop as I didnt like how the program had to be restarted if the input was wrong. 

while True:
    full_name = input('Please enter your full name: ')

# Check if the input is empty
    if not full_name:
        print('You have not entered anything.')
        

# Check if the input has less than 4 characters
    elif len(full_name) < 4:
        print('You have entered less than 4 characters. Please make sure that you have entered your name and surname.')
       

# Check if the input has more than 25 characters
    elif len(full_name) > 25:
        print('You have entered more than 25 characters. Please make sure that you have only entered your full name.')
        

# Check if the input consists of two words
    elif len(full_name.split()) != 2:
        print('Invalid input. Please enter your full name consisting of two words.')
        

# Input is valid
    else:
    # Extract the first and last name from the input
        first_name, last_name = full_name.split()
        print(f'Thank you, {first_name.capitalize()} {last_name.capitalize()}, for entering your full name.')
        break