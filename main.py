#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

#user input the amount of the bill 
bill = float(input("What's was the total  bill? $"))

#user input the percentage of the tip he wants to give
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))

#calculate tip à a percentage 
tip = 1 + (tip / 100)

#input the number of person to split the bill with 
people = int(input("How many people to split the bill ? "))

#calcultate tip per persone and round it to 2 decimal and print it 
tip_per_person = (bill * tip) / people
tip_per_person = round(tip_per_person, 2)

print(f"Each person should pay: ${tip_per_person}")

