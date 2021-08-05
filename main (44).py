def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct! Nice Job!")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("That is incorrect. Guess again:")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Phone")
guess1 = input("What is the most sold phone of 2020?")
check_guess(guess1, "iPhone 11")
guess2 = input("What is the best speced phone of 2021? ")
check_guess(guess2, "Xiaomi Mi 11 Ultra")
guess3 = input("What is the name of Oppo's 2021 Flagship? ")
check_guess(guess3, "Oppo Find X3 Pro")
print("Your Score is "+ str(score))