'''
This code is a simple age calculator that prompts the user for their birth year and 
the current year, calculates their age, and prints it out.
It uses functions to separate the logic for getting the birth year, calculating the age, 
and the main program flow.
The `get_birth_year` function retrieves the user's birth year, the `calculate_age` 
function computes the age based on the birth year and current year, and the `main` function 
orchestrates the flow of the program.
'''  

def get_birth_year():
    return int(input("Enter your birth year: "))

def calculate_age(birth_year, cuurent_year):
    return cuurent_year - birth_year

def main():
    birth_year = get_birth_year()
    cuurent_year = int(input("Enter the current year: "))
    age = calculate_age(birth_year, cuurent_year)
    print("you are %d years old." %age)

if __name__ == "__main__":
    main()
    