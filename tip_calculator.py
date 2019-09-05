# tip calculator with an attempt at error handling
# after reviewing, this script seems unnecessary complicated and
# could be handled by several if, elif statements

bill = float(input("Bill amount? >> "))

if bill <= 0:
    print("Please enter a valid bill amount.")
    exit()
else:
    pass

level_of_service = input("Level of service? good, fair, bad >> ")

if level_of_service not in ('good', 'fair', 'bad'):
    print("Please enter good, fair, or bad.")
    exit()
else:
    pass


def tip_calc(level_of_service):

    if level_of_service == "good":
        tip = 0.20
    elif level_of_service == "fair":
        tip = 0.15
    elif level_of_service == "bad":
        tip = 0.10
    else:
        print("Please enter a valid value.")

    return tip


tip = tip_calc(level_of_service)


def total_bill(tip, bill):

    tip_amount = tip * bill
    total = tip_amount + bill

    return tip_amount, total


# contains a tuple that contains  the tip_amount and the total
total = total_bill(tip, bill)

print(f"Tip Amount: {total[0]:.2f}")
print(f"Total Bill Amount: {total[1]:.2f}")


group_split = int(input("Split how many ways? Enter a number. >> "))

try:
    amt_per_person = total[1] / group_split
    print(f"Amount per person: ${amt_per_person:.2f}")

except ZeroDivisionError:
    print("You cannot divide by Zero.")
    exit()
