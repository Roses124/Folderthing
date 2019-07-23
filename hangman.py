import random
# A list of words that
potential_words = ["apple", "code", "cat", "goldfish", "horse"]
maxfails = 7
fails = 0
word = random.choice(potential_words)
word = word.lower()
print(word)
length = len(word)
current_word = ["_"] * length # TIP: the number of letters should match the word
print(current_word)
# Make it a list of letters for someone to guess
# Use to test your code:
# print(word)
while fails < maxfails:
    guess = input("Guess a letter or word! ")
    iter = 0
    if guess in word:
        for let in word:
            if let == guess or guess == word:
                current_word[iter] = guess
                print(current_word)
            iter += 1
    if ("_") not in current_word or guess == word:
        print("You win!")
        break
    elif guess not in word:
        print(current_word)
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")
# Converts the word to lowercase


# Some useful variables




	# check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
