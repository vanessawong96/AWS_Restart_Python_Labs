#Program to check whether user's input is a palindrome
user_input = input('Enter a set of digits, alphabets, or symbols, or a combination of all. Then, press Enter ')

reverse = user_input[::-1]              
#using the Slicing method, we do not define the start and end so that it will check every character in the user's input
#the step is set to -1 so that it will check each character from the last character to the first character in the user's input, and list them out according to the sequence it was read

if user_input == reverse:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
