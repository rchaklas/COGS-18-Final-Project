#COGS 18 Final Project Raam Chaklashiya
#test_functions.py

import functions

def test_up_left():
	test_eight = functions.FigureEight()
	#Tests to see if when an initial position of [5, 5] is [4, 4] after moving to the left and up.
	assert test_eight.up_left([5, 5]) == [4, 4]

def test_up_right():
	test_eight = functions.FigureEight()
	#Tests to see if when an initial position of [5, 5] is [4, 6] after moving to the right and up.
	assert test_eight.up_right([5, 5]) == [4, 6]

def test_down_left():
	test_eight = functions.FigureEight()
	#Tests to see if when an initial position of [5, 5] is [6, 4] after moving to the left and down.
	assert test_eight.down_left([5, 5]) == [6, 4]

def test_down_right():
	test_eight = functions.FigureEight()
	#Tests to see if when an initial position of [5, 5] is [6, 6] after moving to the right and down.
	assert test_eight.down_right([5, 5]) == [6, 6]
	