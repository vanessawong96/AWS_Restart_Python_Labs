##Class revision##

#Question 1 - use if, elif loop
userReply = input("What day is it today? ")
if userReply == "Friday":
    print("Correct answer! Today is Friday. Weekends are coming!")
elif userReply == "Saturday":
    print("How I wish it was the weekends too.")
elif userReply == "Sunday":
    print("It's not Sunday yet.")
else:
    print("Wrong answer.")

print(" ")

#Question 2 - use while loop
print("There is a $1000 reward in one of three boxes (Box A, Box B, Box C). Pick one box to find out if you win! ")
correctAnswer = "C"
isGuessRight = False
while isGuessRight != True:
    guess = input("Please enter A, B, or C: ")
    if guess == correctAnswer:
        print("Congratulations! You picked the correct box. Here is your $1000 reward.")
        isGuessRight = True
    else:
        print("You picked {}. Wrong box! Try again...".format(guess))
        
print(" ")

#Question 3 - Use lists and tuples and make changes to precreated list

#Example of creating List, and making changes to precreated List
myFavoriteSuperheroList = ["Batman", "Superman", "Baby Groot"]
userReply1 = input("Let me tell you about my favorite superheroes!")
userReply2 = input("My favorite superheroes are " + myFavoriteSuperheroList[0] + ", " + myFavoriteSuperheroList[1] + " and " + myFavoriteSuperheroList[2] + ". ")
userReply3 = input("Two days later, I don't like Baby Groot anymore. ")
myFavoriteSuperheroList[2] = "Wonder Woman"
print(myFavoriteSuperheroList[2] + " is my new favorite Superhero. Bye Baby Groot!")

print(" ")

#Example of Tuple
myFavoriteFoodTuple = ("sushi", "pizza", "burger")
userReply4 = input("Now I will tell you about my favorite food. I will forever love these dishes!" )
print("My favorite food are " + myFavoriteFoodTuple[0] + ", " + myFavoriteFoodTuple[1] + " and " + myFavoriteFoodTuple[2] + "!")

print(" ")

#Question 4 - use for loop
userReply5 = input("Here are some words of encouragement!")
words = ["We", "Have", "A", "One", "Week", "Break", "Starting", "Tomorrow", "!"]
for x in range(len(words)):
    print(words[x])


    


