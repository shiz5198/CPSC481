# Name: Shi Zheng
# Assignment 4
#
#  Trust Fund Buddy
# I just added a little bit to advice the user how long he/she 
# can still last and if its not long enough the program will advide 
# the user to cut down the expanse or find a job


print("""

\t\t\t\tTrust Fund Buddy

Totals is your monthly spending so that your trust fund doesn't
run out (and you're forced to get a real job).

Please enter the requested monthly costs. Since you're rich, ignore
pennies and use only dollar amounts.
"""
      )

trust_fund = 400000
print("Your current trust fund amount is $", trust_fund)

car = int(input("Lamborghini Tune-Ups: $"))
rent = int(input("Manhattan Apartment: $"))
jet = int(input("Privaye Jet Rental: $"))
gifts = int(input("Gifts: $"))
food = int(input("Dining Out: $"))
staff = int(input("Staff(butlters, chif, driver, assistant): $"))
guru = int(input("Personal guru and Coash: $"))
games = int(input("Computer Games: $"))

total = car + rent + jet + gifts + food + staff + guru + games

print("\n Grand Total: $", total)
print("\n Your current trust fund after this month is: $", trust_fund - total)

if trust_fund <= 100:
    print("\n You need to find a job!")
    
count = int(trust_fund/total)
year = 0
month = 0
if count > 12:
    year = int(count/12)
    month = count%12
else:
    month = count
    
print("\n If you continue to spend the same amout of money every month, 
            you will be able to last roughly ", year, "year(s) and ", month, "month(s).")

if year < 20:
    print("\nFriendly advice: You should cut down your expanse or find a job.")
    
input("\n\nPress the enter key to exit.")
