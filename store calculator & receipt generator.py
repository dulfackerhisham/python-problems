# Write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard.
import re

sum = 0
while(True):
    userPrice = input("Enter product price AND Enter 'done' after completation: \n")

    if userPrice.lower() == "done":
        if sum > 0:
            tax_rate = 0.05
            tax = sum * tax_rate
            total = sum + tax

            print(f"product total => {sum} \nGST => {tax} \nTotal = {total}")
        break
    else:
        sum = sum + int(userPrice)
        print(f"total price so far => {sum}")
    
    if not re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)$', userPrice):
        print("Invalid input. Please enter a valid number OR 'done'. ")
        continue