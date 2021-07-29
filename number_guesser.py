import random

no_of_attempts = 5
the_number = random.randint(0, 50)

for attempt in range(0, no_of_attempts):
    guess = int(input("Guess the number (0-50): "))

    switcher = [
        ["The number is lesser than 25", "The number is greater than or equal to 25"],
        "The number is prime",
        "dumb",
        "dumb",
        ["The number is odd", "The number is even"]
        ]

    if the_number == guess:
        if attempt == 0:    
            print(f"You guessed it in the first attempt, {the_number}!!!!")
            break
        else:
            print(f"You guessed the number {the_number} in the attempt no. {attempt+1}")
            break

    if attempt == 0:
        if the_number < 25:
            print(switcher[0][0])
        else:
            print(switcher[0][1])

    if attempt == 1:
        divisors = [i for i in range(2, the_number) if the_number % i == 0]
        length = len(divisors)-1
        choose = random.randint(0, length)
        the_divisor = divisors[choose]
        if the_number % the_divisor == 0:
            print(f"The number is divisible by {the_divisor}")
        else:
            print(switcher[1])

    if attempt == 2:
        if the_number % 5 != 0 or the_number % 10 != 0:
            start = (the_number // 10) * 10
            end = start + 10
            print(f"The number is between {start} and {end}")
        else:
            print("The number is a multiple of 5.")

    if attempt == 3:
        if the_number % 5 != 0 or the_number % 10 != 0:
            start = (the_number // 10) * 10
            end = start + 10
            mid = (start + end)/2
            if the_number < mid:
                print(f"The number is less than {mid}")
            else:
                print(f"The number is greater than {mid}")
        else:
            print(f"The number is between{the_number - 5} and {the_number + 5}")

    if attempt == 4:
        if the_number % 2 != 0:
            print(switcher[4][0])
        else:
            print(switcher[4][1])

else:
    print(f"You lost! The number was {the_number}")
        
        

