import csv
import random

print(f'Finding a MetaCritic comment....\r')

with open('metacritic_game_user_comments.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter = ',')

    header = next(csvreader)

    # Had to change this to a explicitly defined max number
    # apparently two for loops through the file is too many?
    # old code:
    # comment_num = random.randrange(0, sum(1 for row in csvreader))

    comment_num = random.randrange(0, 283982)

    # print(f'random number: {comment_num}')

    for row in csvreader:
        if int(row[0]) == comment_num:
            game = row[1]
            user_score = row[3]
            user_comment = row[4]

    f.close()

with open('metacritic_game_info.csv', 'r') as info:
    inforeader = csv.reader(info, delimiter = ',')

    for row in inforeader:
        if game == row[1]:
            metascore = row[6]
            avg_user = row[7]
    
    info.close()

    print(f"\rThis user rated this game a score of {user_score}.")
    print(f"Here's what they had to say about it:\r{user_comment}\r")
    print(f'This game has a metascore of {metascore} and an average user score of {avg_user}.\r')
    print(f"What game is this?")

    guess_again = 'y'

    while guess_again == 'y':
        guess = input(f"Enter a game: ")

        if guess in game:
            print(f'\rYes!')
            guess_again = 'n'
        else:
            guess_again = input(f'\rNope. Want to try again? (y/n) ')
    else:
        print(f'It was {game}.')
        print(f'\rThanks for playing!')
