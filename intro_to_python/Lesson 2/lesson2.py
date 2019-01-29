#Get the name of a user
#value = input ("Please enter your name and age")
#print (value)

#age = eval(input ("Please enter your age"))
#future_age = age + 10
#print (future_age)

#import math
#print ("the value of pi is")
#print (math.pi)

#print ("There's even another way")
#print ("to do power, with math.pow")
#print (math.pow (2, 2))

#print ("New " + "York")
#print ("and over " * 6)

#word = "My words are important!"
#print (len(word))

#indexing and slicing

#phrase = "Python rocks!"
#print (phrase [0] )

#phrase = "Python rocks!"
#print (phrase [1:3] )

#phrase = "Python rocks!"
#print (phrase [7:12] )

#phrase = "Python rocks!"
#print (phrase [7:] )

#This --> phrase [0] = 'p' won't work because indexing strings only use it to access the characters
#phrase = "Python rocks!"
#so you can just do it this way
#print ('p' + phrase [1:])

#value1 = 1
#value2 = 2
#print (value1, end=" ")
#print (value2, end="")

#This program takes the name of user, number of books they've this year (and past 5 years), and the name of one book read
#("Hello + user_name, I see you've read book_names books. Thats a lot of books!")
#user_name = input("Hi, what is your name? ")
#bookRead = eval(input("How many books have you read this year? "))
#booksReadRastFiveYears = eval(input("How about the past 5 years? "))
#print ("Wow!" + bookRead + "! " "Thats a lot of books!")
#print (books_read_2018 [27:38] + books_read_2018 + "books" + books_read_2018 [39:])
#print ("Could you name one of those books?")
#book_names = input("Enter the name of a book you read this year: ")
#print ("Wow " + user_name + "! " + book_names + "sounds like a great book!")

# Introduction to Python Programming
# Lesson 02 Assignment
# Sample Solution

# Get phrase from user
phrase = input("Please enter a phrase: ")

# Now get starting and ending positions
startNum = eval(input("Please enter the starting position: "))
endNum = eval(input("Please enter the ending position: "))

# Finally print out the slice
print (phrase[startNum:endNum+1])

# NOTE: Some may want to show the character at the last position
#   to the user.  In that case, the above print statement would be:
# print (phrase[len(phrase)-1:len(phrase)])

