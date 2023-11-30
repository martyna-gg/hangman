import random
print('H A N G M A N \n')

# printing menu
decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
print()

# setting scores recording
wins = 0
losts = 0

# managing the menu decision
# case of choosing incorrect option
while decision not in ['play', 'results', 'exit']:
    decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
    print()
while decision != 'exit':
    # decision to print the scores
    if decision == 'results':
        print(f'You won: {wins} times. \nYou lost: {losts} times.\n')
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
        print()
        # case of choosing incorrect option 
        while decision not in ['play', 'results', 'exit']:
            decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
            print()
    # decision to start the game
    if decision == 'play':

        f = open("./words.txt", "r")  # opening the wordlist
        game_list = (f.read()).split()
        game_choice = random.choice(game_list)  # selecting the random word
        hint = '-'*(len(game_choice))  # setting and printing the game board
        print(hint + '\n')

        i = 0  # number of attempts (player has 8 attempts)
        answers = [] #  list of chosen letters
        while i < 8:
            correct = 0
            while correct < 3:
                correct = 0  # checking if chosen letter is correct
                ans = input('Input a letter: > ')
                print()
                
                if len(ans) != 1:  # if it is a single lerrer
                    print(hint + '\n')
                    print('Please, input a single letter.\n')
                    continue
                else:
                    correct += 1  # if it is a lowercase one
                if ans.islower():
                    correct += 1
                else:
                    print(hint + '\n')
                    print('Please, enter a lowercase letter from the English alphabet.\n')
                    continue
                if ans in answers:  # if it was not chosen before
                    print(hint + '\n')
                    print("You've already guessed this letter.\n")
                    continue
                else:
                    answers.append(ans)
                    correct += 1
            
            if ans not in game_choice:  # if choice is not correct
                print(hint + '\n')
                print("That letter doesn't appear in the word.\n")
                i += 1
            else:
                for j in range(len(game_choice)):  # adding correct letter to the game board
                    if game_choice[j] == ans:
                        hint_lst = list(hint)
                        hint_lst[j] = ans
                        hint = "".join(hint_lst)
                print(hint + '\n')         
            if '-' not in hint:  # checking for win
                print(f'You guessed the word {hint}! \nYou survived!\n')
                wins += 1
                i = 9
        if '-' in hint:  # checking for loss
            print('You lost! The keyword to guess was:', game_choice + '\n')
            losts += 1
        # repeating menu after finished game
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
        print()
        while decision not in ['play', 'results', 'exit']:
            decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
            print()