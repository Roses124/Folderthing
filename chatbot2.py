# --- Define your functions below! ---
import random
sports = ["tennis", "baseball", "softball", "basketball", "track", "swim", "dance", "soccer", "football", "field hocky", "lacrosse"]
answer = random.choice(sports)
answer = answer.lower()
valid_greetings = ["hi", "hey", "hello", "sup", "howdy"]
goodbyes = ["see ya", "bye", "got to go", "byebye", "cya", "goodbye"]

def is_valid_input(answer):
    if answer in valid_greetings:
        return True
    else:
        return False

def valid_sport():
    if answer in sports:
        return True
    else:
        return False

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
    valid_sport()
    if answer in sports:
        print("I love " + str(answer) + " too! What a coincidance!")
def process(answer):
    is_valid_input(answer)
    iter = 0
    if answer in valid_greetings:
        response(sports)
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
        if answer in goodbyes:
            goodbye()
            break



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
