import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

""" The Player class is the parent class for all of the Players
in this game """


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1Score = 0
        self.p2Score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{self.p1.name}: {move1}, Computer: {move2}")
        result1 = beats(move1, move2)
        result2 = beats(move2, move1)
        if result1 is True:
            self.p1Score += 1
        elif result2 is True:
            self.p2Score += 1
        print(f"{self.p1.name}: {self.p1Score}, Computer: {self.p2Score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print("")
            print(f"Round {round}:")
            self.play_round()
        print("")
        if self.p1Score > self.p2Score:
            print(f"{self.p1.name} Have Won!!")
        elif self.p1Score == self.p2Score:
            print("It's A Draw!!")
        else:
            print("Computer Have Won!!")
        print(f"{self.p1.name}: {self.p1Score}, Computer: {self.p2Score}")
        print("Game over!")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name

    def move(self):
        myMove = input("Enter Your Move ('rock', 'paper', 'scissors'): ")
        while True:
            if myMove in moves:
                break
            print("Invalid Move")
            myMove = input("Enter Your Move again: ")
        return myMove


class ReflectPlayer(Player):
    def __init__(self):
        self.myMove = random.choice(moves)

    def move(self):
        return self.myMove

    def learn(self, my_move, their_move):
        self.myMove = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.myMove = random.choice(moves)

    def move(self):
        if self.myMove == 'rock':
            return 'paper'
        elif self.myMove == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, their_move):
        self.myMove = my_move


if __name__ == '__main__':
    level = ['easy', 'normal', 'hard', 'expert']
    name = input("Hello :), Enter your name: ")
    level_choice = input("Choise a level (Easy, Normal, Hard, Expert): ")
    while True:
        if level_choice.lower() in level:
            break
        else:
            print("Invalid level")
            level_choice = input("Choise again: ")
    if level_choice == 'easy':
        Computer = Player()
    elif level_choice == 'normal':
        Computer = RandomPlayer()
    elif level_choice == 'hard':
        Computer = CyclePlayer()
    else:
        Computer = ReflectPlayer()
    game = Game(HumanPlayer(name), Computer)
    game.play_game()
