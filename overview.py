import random

# A list of words that 
potential_words = ["Calico", "Siamese", "Ragdoll", "Sphynx"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower("calico", "siamese", "ragdoll", "sphynx")

# Make it a list of letters for someone to guess
current_word = ["c", "a", "l", "i", "o", "s", "a", "m", "e", "r", "d", "p", "h", "y", "n", "x"] # TIP: the number of letters should match the word

# Some useful variables
guesses = [10]
maxfails = 10
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
    guesses.append(guess)

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
