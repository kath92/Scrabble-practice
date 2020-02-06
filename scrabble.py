# Cheat sheet: https://github.com/adrielklein/scrabble-word-finder/blob/master/app/finders/word_finder.py
# https://codereview.stackexchange.com/questions/172263/simplifying-a-scrabble-word-finder-python/172288
import random
from collections import Counter

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
letter_to_points["#"] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

##########################################

players_to_points = {}
def update_points_totals():
    """
    Return total number of points
    """
    for key, value in player_to_word.items():
        player_points = 0
        for word in value:
            player_points += score_word(word)
    players_to_points[player] = player_points
#update_points_totals()
#print(players_to_points)

###########################################

def play_word(word):
    players_word_list[player].append(word)
    update_points_totals()

###########################################
def count_total(word_dict):
    total = 0
    for word, score in word_dict.items():
        total += score
    return total


# Ask for user name, print some letters and then save the score
def give_out_letters(letter_list):
    return random.sample(letter_list, k=7)


def swap_letter(user_letter):
    pass

def play():
    pass

############### RECOGNISING WORDS ##########

# Open vocabulary bank and create a dictionary using counter
with open('words.txt') as fin:
    lines = (word.strip().upper() for word in fin)
    words = [(word, Counter(word)) for word in lines]
fin.close()

def practise(words):
    """
    Takes in a dict with word bank and counter function applied to the words
    """
    user_ans = ""
    score = 0
    total_score = 0
    player_words_and_scores = {}
    game_on = True

    while True:
        # Generate letters for the user and print these:
        random_words_user_list = give_out_letters(letters)
        print("Your letters are as follows: ", random_words_user_list)

        # Join the element of the list of letters into a string
        random_string = ""

        for letter in random_words_user_list:
            random_string += " ".join(letter)

        possible_solution_list = []

        rack = Counter(random_string)
        for scrabble_word, letter_count in words:
            # Using length here to limit output for example purposes; the larger thr len, the less words we create
            if len(scrabble_word) >= 2 and not (letter_count - rack):
                possible_solution_list.append(scrabble_word)
        if not possible_solution_list:
            possible_solution_list.append("Sorry, there was no word that could have been created!")

        while game_on:
            print("Your letters: ", random_words_user_list)
            user_ans = input("Press 'q' to quit, 'c' to change the word or 'p' to see possible answers.\nEnter a word: ")
            print("Veryfing your answer...")

            if user_ans.lower() == "c":
                print("Changing the set of letters...")
                break
            elif user_ans.upper() in possible_solution_list:
                score = score_word(user_ans.upper())
                total_score += score
                player_words_and_scores[user_ans.upper()] = score
                print("Well done! Your score is {0} and your total score is {1}".format(score, total_score))
                break
            elif user_ans.lower() == 'q':
                game_on = False
                return "Your total score was {0}!\n Good-bye!".format(total_score)
            elif user_ans.lower() == 'p':
                print("Here is a list of possible solutions:\n", possible_solution_list)
                break
            else:
                print("Wrong answer!\n")
                #user_ans = input("")

print(practise(words))
############### TESTING AREA ####################

# user_ans = ""
# play = True

# c = ""
# while not c == "c":
#
#     print("looping...")
#     c = "c"

#
#
# while play:
#     user_ans = input("Enter a word: ")
#     if user_ans == "c" or user_ans == "C":
#         print("breaking the loop...")
#         play = False

############### IDEAS/ISSUES ############################

# Create 2 modes = practice and play againt 'the computer'. How to immplement grid there...
# How to create grid and graphical representation? Maybe do sudoku first...
# Learn UI... dragging letters...
