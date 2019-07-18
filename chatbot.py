# --- Define your functions below! ---
import random
sports = ["tennis", "baseball", "softball", "basketball", "track", "swim", "dance", "soccer", "football", "field hockey", "lacrosse"]
answer = random.choice(sports)
answer = answer.lower()
def goodbye():
    print("It was nice to talk to you!")
    print("I'll talk to you later!")

def intro():
    print("Hi! Welcome to my chat!")

def greeting():
    print("It's so nice to meet you!")

def default():
    print("That's neat! Anything else? ")

def response(answer):
    print("'sup! What sport do you play? ")

    if answer in sports:
        print("I love " + str(answer) + " too! What a coincidance!")
def process(answer):
    iter = 0
    if answer == "hi":
        response(sports)
        sports[iter] = answer
    elif answer == "hello":
        response(answer)
        sports[iter] = answer
    elif answer == "hey":
        response(answer)
        sports[iter] = answer
    else:
        default()
        response(answer)
        sports[iter] = answer
    iter =+ 1

# --- Put your main program below! ---
def main():
    intro()
    greeting()
    while True:
        answer = input("(What will you say?) ")
        process(answer)
        if answer == "i have to go":
            goodbye()
            break
        elif answer == "bye":
            goodbye()
            break
        elif answer == "see ya":
            goodbye()
            break
        elif answer == "goodbye":
            goodbye()
            break


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
