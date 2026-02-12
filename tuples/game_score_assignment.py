player = input("please enter you name: ")
game_played = int(input("please enter how many games you have played until now:"))
total_score = int(input("please enter your total score of the games: "))
average_score = total_score/game_played
print(f" player id: {player}\n has played: {game_played} games \n the total score is: {total_score} \n the average score is: {average_score}") 