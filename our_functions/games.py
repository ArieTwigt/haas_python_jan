import random

class Game:
    
    game_type = "dice"
    players = []

    def __init__(self, game_name):
        self.game_name = game_name
        self.players   = []
        
    
    
    def add_player(self, player):
        self.players.append(player)
    

    def __repr__(self):
        intro = f"A game of type {self.game_type}, with the name {self.game_name}, current players: {self.players}"
        return intro


    def play_game(self):
        for dice in self.players:
           total_throws = 5

           while total_throws > 0:
               dice.throw_dice()
               total_throws -= 1

    
    def calc_game_scores(self):
        score_card_list = []
        for dice in self.players:
            dice.calc_score()
            score_card = dice.create_score_card()
            score_card_list.append(score_card)

        return score_card_list



class DiceBlock(Game):

    # default atrributes
    throws = []


    def __init__(self, player_name, dice_range=6):
        dice_range = list(range(1, dice_range  + 1))
        self.dice_range = dice_range
        self.player_name = player_name
        self.throws = []
        pass

    
    def throw_dice(self):
        result = random.choice(self.dice_range)
        print(f"You threw {result}!")    
        self.throws.append(result)


    def calc_score(self, print_score=False):
        score = sum(self.throws)
        self.score = score
        if print_score:
            print(f"Your score is {score}")


    def create_score_card(self):
        score_card = f"\n\nScore of player {self.player_name}\n"
        score_card += "-" * 5       

        for idx, value in enumerate(self.throws):
            score_line = f"\n{idx + 1}: score: {value}"
            score_card += score_line

        score_card += "\n"
        score_card += "-" * 5    

        # calc score 
        self.calc_score()  
        score_card += f"\nTotal score: {self.score}\n\n"      

        print(score_card)
        return score_card

    
    def __repr__(self):
        introduction = f"Dice block of: {self.player_name}"
        return introduction
    

    pass