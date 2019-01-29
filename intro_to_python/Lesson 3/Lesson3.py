#Decisions

#if statments

#age = "me"
#if age == "you":
#    print("ten")
#print("how's that?")

#letter = "Z"
#if letter < "d":
#    print("less than d")

#if letter > "d":
#    print("greater than d")

#if letter == "d":
#    print("equal to")

#else statements

#age = 32

##if else statement

#if age >= 18:
#    print("Congratulations")
#    print("You are old enough to vote")

#else:
#    print("Sorry")
#    print("You are not old enought to vote")

##nested if else statement known as multiway since program has multiple paths it can take
##when coding multiway ifs with nested loops, once a condition evaluates to true, you break out of the if structure completely.
#year = eval(input("Enter year: "))

#if year == 1:
#    print("freshman")
#else:
#    if year == 2:
#        print("sophmore")
#    else:
#        if year == 3:
#            print("junoir")
#        else:
#            if year == 4:
#                print("senior")

##tab indents can get confusing so elif has the same functionalility and is easier to read and keep track of.

#year = eval(input("Enter year: "))
#if year == 1:
#   print ("Freshman")
#elif year == 2:
#   print ("Sophomore")
#elif year == 3:
#   print ("Junior")
#elif year == 4:
#   print ("Senior")

##Logic operaters

#age = eval(input("How old are you? "))
#registered = input("are you registered? (y/n) ")
#if age >= 18:
#   if registered == "y":
#      print("you are ready to vote!")
#   else:
#      print("you are not ready yet")


##evaluate two conditions at once with compound conditions.

#age = eval(input("How old are you? "))
#registered = input("are you registered? (y/n) ")

#if age >= 18 and registered == "y":
#      print("you are ready to vote!")
#else:
#      print("you are not ready yet")

#answer = input("Enter a letter: ")
#if answer == 'y' or 'Y':
#   print("you entered 'y' or 'Y'")


##This program asks user hourly rate and hours worked for the week, than calculates pay

#rate = eval(input("hourly rate: "))
#hours = eval(input("hours worked this week: "))

#if hours < 40:
#   pay = rate * hours

#else:
#   pay = rate * hours
#   overtimeHours = hours - 40
#   overtimePay = overtimeHours * (rate * 0.5)
#   pay = pay + overtimePay

#print("Your total pay for the week is:", pay)
