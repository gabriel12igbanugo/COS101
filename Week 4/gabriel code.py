# MULTIPLICATION TABLE


while True:
    print ()

    number= (input("input a number (or enter zero to quit):"))

    if number =="exit":
        print("Exiting program thank you")
        break
    
    

    if number<="1":
        print("Error Error please chose a greater number!")
        continue

    for multiplier in range(1,12):
        result=number*multiplier
        print(f"{number}x{multiplier}={result}")
    

    print()
    print("=======================")
