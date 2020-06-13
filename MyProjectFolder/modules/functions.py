#COGS 18 Final Project Raam Chaklashiya
#functions.py

import random
from time import sleep
from IPython.display import clear_output


#add_lists function taken from assignment 4
def add_lists(list1, list2):
    
    output = []
    
    for it1, it2 in zip(list1, list2):
        element_sum = it1 + it2
        output.append(element_sum)
    return output


#check_bounds function taken from assignment 4
def check_bounds(position, size):
    
    for element in position:
        if element < 0 or element >= size:
            return False
    return True


#play_board function taken from assignment 4
def play_board(bots, n_iter = 25, grid_size = 5, sleep_time = 0.3):
    """Run a bot across a board.
    
    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    """
    
    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]
    
    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size

    for it in range(n_iter):

        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]
        
        # Add bot(s) to the grid
        for bot in bots:
            grid_list[bot.position[0]][bot.position[1]] = bot.character    

        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)

        # Update bot position(s) for next turn
        for bot in bots:
            bot.move()


#Modified version of Bot from assignment 4, same code except self.moves is modified to only allow for diagonal movement
class DiagonalBot():
    
    def __init__(self, character = 8982):
        self.character = chr(character)
        self.position = [0, 0]
        self.moves = [[-1, -1], [1, -1], [-1, 1], [1, 1]]
        self.grid_size = None


#Code from WanderBot from assignment 4, same code except uses the diagonal movement of DiagonalBot
class WanderDiagonal(DiagonalBot):
    
    def __init__(self, character = 8982):
        super().__init__(character = 8982)
    
    def wander(self):

        has_new_pos = False

        while not has_new_pos:
            move = random.choice(self.moves)
            new_pos = add_lists(move, self.position)
            has_new_pos = check_bounds(new_pos, self.grid_size)
        return new_pos
        
    def move(self):
        self.position = self.wander()
        

#Code from ExploreBot from assignment 4 with changes only to move_prob and sets a new starting position
class StraightDiagonal(DiagonalBot):
    
    def __init__(self, character = 8982, move_prob = .85, last_move = None):
        super().__init__(character = 8982)
        
        self.move_prob = move_prob
        self.last_move = last_move
        #Also starts at an off-centered position of [0, 1] to help avoid going back and forth in a straight line
        self.position = [0, 1]

    def biased_choice(self):
       
        move = None

        if self.last_move != None:
            if random.random() < self.move_prob:
                move = self.last_move
        if move == None:
            move = random.choice(self.moves)
        return move

    def explore(self):
        
        has_new_pos = False

        while not has_new_pos:
            move = self.biased_choice()
            new_pos = add_lists(move, self.position)
            has_new_pos = check_bounds(new_pos, self.grid_size)
            self.last_move = move
        return new_pos
        
    def move(self):

        self.position = self.explore()
        

#Original Bot that moves in the shape of an "8"
class FigureEight(DiagonalBot):

    def __init__(self, character = 8982, counter = 0):
        super().__init__(character = 8982)

        self.counter = counter
        #Starts at a central posistion of [6, 6] in a 13 by 13 grid so that the bot does not go out of bounds
        self.position = [6, 6]

    #Method that moves the bot 1 space up and left diagonally
    #test_pos is included for the test functions to input values and check if the right move is made
    def up_left(self, test_pos = None):

        self.test_pos = test_pos
        move = [-1, -1]

        #only runs when testing values
        if test_pos != None:
        	self.position = test_pos
        	new_pos = add_lists(move, self.position)
        	return new_pos

        new_pos = add_lists(move, self.position)
        return new_pos

    #Method that moves the bot 1 space down and left diagonally
    def down_left(self, test_pos = None):

        self.test_pos = test_pos
        move = [1, -1]

        #only runs when testing values
        if test_pos != None:
        	self.position = test_pos
        	new_pos = add_lists(move, self.position)
        	return new_pos

        new_pos = add_lists(move, self.position)
        return new_pos

    #Method that moves the bot 1 space up and right diagonally
    def up_right(self, test_pos = None):
        
        self.test_pos = test_pos
        move = [-1, 1]

        #only runs when testing values
        if test_pos != None:
        	self.position = test_pos
        	new_pos = add_lists(move, self.position)
        	return new_pos

        new_pos = add_lists(move, self.position)
        return new_pos

    #Method that moves the bot 1 space down and right diagonally
    def down_right(self, test_pos = None):
        
        self.test_pos = test_pos
        move = [1, 1]

        #only runs when testing values
        if test_pos != None:
        	self.position = test_pos
        	new_pos = add_lists(move, self.position)
        	return new_pos

        new_pos = add_lists(move, self.position)
        return new_pos

    #Instructions for the bot to move in the shape of an "8"
    def cycle(self):
        
        #Move 3 spaces up and left
        if self.counter < 3:
            move = self.up_left()
            self.counter += 1
            return move

        #Move 3 spaces up and right
        elif self.counter >= 3 and self.counter < 6:
            move = self.up_right()
            self.counter += 1
            return move

        #Move 3 spaces down and right
        elif self.counter >= 6 and self.counter < 9:
            move = self.down_right()
            self.counter += 1
            return move

        #Move 6 spaces down and left
        elif self.counter >= 9 and self.counter < 15:
            move = self.down_left()
            self.counter += 1
            return move

        #Move 3 spaces down and right
        elif self.counter >= 15 and self.counter < 18:
            move = self.down_right()
            self.counter += 1
            return move

        #Move 3 spaces up and right
        elif self.counter >= 18 and self.counter < 21:
            move = self.up_right()
            self.counter += 1
            return move

        #Move 3 spaces up and left back to the original position
        elif self.counter >= 21 and self.counter < 24:
            move = self.up_left()
            self.counter += 1
            return move   

    #Method that moves the bot
    def move(self):

        self.position = self.cycle()