##This program prints a table of Celsius to Fahrenheit equivalents between 0 and 100 in increments of 10 degrees

Celsius = 0
def convert_to_fahrenheit(Celsius):
    fahrenheit = 9.0/5.0 * Celsius + 32
    return fahrenheit

print ("Celsius to Fahrenheit")
for cel in range(0, 101, 10):
    print (cel, "to", convert_to_fahrenheit(cel))

#Celsius = eval(input("Enter Celsius temperture you want to convert bitch: "))

#if Celsius >= 0 and Celsius <= 100:
