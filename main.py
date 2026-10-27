"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    
    return round(annual_cost / SEMESTERS_PER_YEAR, 2)


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return round(annual_cost / MONTHS_PER_YEAR, 2)


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return round(annual_cost / SEMESTERS_PER_YEAR / CLASS_DAYS_PER_SEMESTER, 2)


def cost_per_credit(annual_cost, credits):

    return round(annual_cost / SEMESTERS_PER_YEAR / credits, 2)


def cost_per_class(annual_cost, credits):
    per_credit = annual_cost / SEMESTERS_PER_YEAR / credits
    return round(per_credit * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER, 2)


def ask_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Yeah, that's not going to work. Please enter a POSITIVE number.")

def menu():
    print("Cost of College Menu")
    print("1. Calculate cost per semester")
    print("2. Calculate cost per month")
    print("3. Calculate cost per day")
    print("4. Calculate cost per credit")
    print("5. Calculate cost per class")
    print("6. Is CS 1430 worth it?")
    print("Q. Quit")


def worth_it(annual_cost, credits):
    per_class = cost_per_class(annual_cost, credits)
    course_total = round(per_class * CS1430_MEETINGS_PER_SEMESTER, 2)

    print()
    print(" WORTH IT?")
    print(f"A single CS 1430 meeting costs you ${per_class:,.2f}")
    print(f"The whole course (45 meetings) costs ${course_total:,.2f}")

    attended = ask_number(
        "How many CS 1430 meetings have you attended so far? ")
    spent = round(per_class * attended, 2)
    print(f"Meetings attended: {attended:.0f}")
    print(f"Money already spent on those meetings: ${spent:,.2f}")

    if attended >= CS1430_MEETINGS_PER_SEMESTER / 2:
        print("You've used more than half the meetings.")
    else:
        print("Plenty of meetings left.")

def main():
    annual_cost = ask_number("Enter the annual cost of college: ")
    credits = ask_number("Enter the number of credits for the semester: ")

    while True:
        menu()
        # Show your menu here.

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost)}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(annual_cost, credits)}")
        elif choice == "6":
            worth_it(annual_cost, credits)
        else:
            print("No, no. You have to choose 1-6 or Q.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
