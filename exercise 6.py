#question no.1

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    rolls = 0
    result = None

    while result != 6:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")

    print(f"Congratulations! It took {rolls} rolls to get a 6.")

if __name__ == "__main__":
    main()




#question no.2
import random

def roll_dice(sides):
    rolls = 0
    while True:
        result = random.randint(1, sides)
        rolls += 1
        print(f"You rolled a {result} on a {sides}-sided dice.")
        if result == sides:
            break
    return rolls

def main():
    max_sides = int(input("Enter the maximum number of sides on the dice: "))
    rolls = roll_dice(max_sides)
    print(f"It took {rolls} rolls to get the maximum number on the {max_sides}-sided dice.")

if __name__ == "__main__":
    main()




#question no.3

# 1 gallon is = 3.78541 liters
def gallons_to_liters(gallons):
    return gallons * 3.78541


def main():
    while True:

        gallons = float(input("Enter the volume in gallons (negative value to exit): "))
        if gallons < 0:
            print("Exiting the program.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equivalent to {liters:.2f} liters.")

if __name__ == "__main__":
    main()



# question no.4
def sum_of_list(numbers):
    return sum(numbers)


def main():
    test_list = [1, 77, 3, 87, 33]
    total = sum_of_list(test_list)

    print(f"The sum of the list {test_list} is: {total}")

if __name__ == "__main__":
    main()


# question no. 5

def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
def main():

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,34,66,98,100]
    filtered_list = remove_odd_numbers(original_list)

    print(f"Original list: {original_list}")
    print(f"Filtered list (no odd numbers): {filtered_list}")


if __name__ == "__main__":
    main()
