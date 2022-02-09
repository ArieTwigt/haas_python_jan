#%% Define the class
class Person:

    # default attributes
    type = "Human"

    # inital attributes
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age  = age


    # class methods
    def add_birthday(self):
        old_age = self.age
        self.age += 1
        print(f"Happy birthday, you turned from {old_age} to {self.age}!")


    def reset_age(self):
        self.age = 0
        print("Born again!")

    
    def __repr__(self):
        intro = f"This is a {self.type}\nThe name is {self.name}\nLives in {self.city}" 
        return intro


# %% Define person based on class
person_1 = Person("Jan", "Rotterdam", 20)


#%%
person_1


#%%
person_2.add_birthday()

#%%
person_2.reset_age()


#%%
add_birthday()






# %%
person_2.type
# %%
person_3 = Person(city="London", name="James")
# %%
person_3.city
# %%
person_2.city
# %%
person_list = [person_2, person_3]
# %%
person_list[0].name

#%%
import random
import math

# %%
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
    

    pass



#%%
dice_1 = DiceBlock("Arie")
dice_2 = DiceBlock("Jan")

#%%
dices_list = [dice_1, dice_2]

#%%

for dice in dices_list:
    total_throws = 5

    while total_throws > 0:
        dice.throw_dice()
        total_throws -= 1

#%%
for dice in dices_list:
    dice.calc_score()
    dice.create_score_card()



# %%
class Game:
    game_type = "dice"
    players = []

    def __init__(self, game_name):
        self.game_name = game_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


    def play_game(self):
        for dice in self.players:
            print(f"\nPlayer: {dice.player_name}\n")
            total_throws = 5
        
            while total_throws > 0:
                dice.throw_dice()
                total_throws -= 1


    def calc_scores(self):
        for dice in self.players:
            dice.calc_score()
            dice.create_score_card()






#%%
my_game = Game("Game 1")


#%%
dice_1 = DiceBlock("Player A")
dice_2 = DiceBlock("Player B")
dice_3 = DiceBlock("Player B")

#%%
my_game.add_player(dice_1)
my_game.add_player(dice_2)
my_game.add_player(dice_3)
# %%

# %%
my_game.play_game()
# %%
my_game.calc_scores()
# %%
dice_1.game_type

# %%
