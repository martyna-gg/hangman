import random
print('H A N G M A N \n')

decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
wins = 0
losts = 0
while decision not in ['play', 'results', 'exit']:
    decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
while decision != 'exit':
    if decision == 'results':
        print(f'You won: {wins} times. \nYou lost: {losts} times.')
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        while decision not in ['play', 'results', 'exit']:
            decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if decision == 'play':

        f = open("/home/marti/ws/hangman/words.txt", "r")
        game_list = (f.read()).split()
        game_choice = random.choice(game_list)
        hint = '-'*(len(game_choice))

        i = 0
        answears = []
        while i < 8:
            print(hint)
            correct = 0
            while correct < 3:
                correct = 0
                ans = input('Input a letter: > ')
                
                if len(ans) != 1:
                    print(hint)
                    print('Please, input a single letter.')
                    continue
                else:
                    correct += 1
                if ans.islower():
                    correct += 1
                else:
                    print(hint)
                    print('Please, enter a lowercase letter from the English alphabet.')
                    continue
                if ans in answears:
                    print(hint)
                    print("You've already guessed this letter.")
                    continue
                else:
                    answears.append(ans)
                    correct += 1
            
            if ans not in game_choice:
                print(hint)
                print("That letter doesn't appear in the word.\n")
                i += 1
            else:
                for j in range(len(game_choice)):
                    if game_choice[j] == ans:
                        hint_lst = list(hint)
                        hint_lst[j] = ans
                        hint = "".join(hint_lst)
                        print('\n')         
            if '-' not in hint:
                print(f'You guessed the word {hint}! \nYou survived!')
                wins += 1
                i = 9
        if '-' in hint:
            print('You lost! The keyword to guess was:', game_choice)
            losts += 1
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        while decision not in ['play', 'results', 'exit']:
            decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')