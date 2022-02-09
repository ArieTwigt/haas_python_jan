from our_functions.games import Game, DiceBlock


if __name__ == "__main__":
    
    # create game
    my_game = Game("Our Game")

    # create players
    dice_1 = DiceBlock("Player Arie")
    dice_2 = DiceBlock("Player Jan")

    # add players to game
    my_game.add_player(dice_1)
    my_game.add_player(dice_2)

    # play game
    my_game.play_game()

    # calc and display the scores
    my_game.calc_game_scores()
