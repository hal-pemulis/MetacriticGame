import csv
import random

with open('metacritic_game_user_comments.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter = ',')

    header = next(csvreader)

    comment_num = random.randrange(0, sum(1 for row in csvreader))

    print(f'random number: {comment_num}')

    for row in csvreader:
        if int(row[0]) == comment_num:
            game = row[1]
            user_score = row[3]
            user_comment = row[4]

    # Code is breaking here...
    # it's correctly selecting a random number within in the CSV's range...
    # but it's not matching that number with row[0] correctly
    print(game)

    print(f"This user rated this game a score of {user_score}.")
    print(f"Here's what they had to say about it:\r{user_comment}\r")
    print(f"What game is this?")

    guess_again = 'y'

    while guess_again == 'y':
        guess = input(f"Enter a game: ")

        if guess in game:
            print(f'Yes! It was {game}!')
        else:
            guess_again = (f'Nope. Want to try again? (y/n) ')
    else:
        print(f'Thanks for playing!')
