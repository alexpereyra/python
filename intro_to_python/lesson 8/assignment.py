
greg_please = []
greg_input = 0

while greg_input >= 0 :
    greg_input = eval(input("Input some numbers (-999 to exit): "))
    greg_please.append(greg_input)
    if greg_input == -999:
        break    

greg_please.remove(-999)
print ("of the numbers you input: ", greg_please )

greg_avg = sum(greg_please) / len(greg_please)
    
print ("The average is: ", greg_avg)
