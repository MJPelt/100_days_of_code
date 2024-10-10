##Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was your bill? "))
tip = int(input("What percentage would you like to tip? 10 15 20 25 "))
party = int(input("How many people will the bill be split with? "))
after_tip = bill *  (tip / 100 + 1)

print(f"Each person should pay: ${round(after_tip / party, 2)}")