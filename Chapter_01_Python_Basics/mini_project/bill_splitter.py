total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))

amount_per_person = total_bill / num_people

print(f"the total bill per person is {amount_per_person:.2f}")