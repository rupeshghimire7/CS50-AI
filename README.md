# CS50-AI

This repository is for learning AI. CS50's Introduction to Artificial Intelligence is a course provided by Harvard University.
I have taken this course from edX, a learning platform.
In this repository, I will be uploading the projects related to the course on various topics.

## 0. Project 0


#### 0.1 Degree

**Understanding**

The distribution code contains two sets of CSV data files: one set in the large directory and one set in the small directory. Each contains files with the same names, and the same structure, but small is a much smaller dataset for ease of testing and experimentation.

Each dataset consists of three CSV files. A CSV file, if unfamiliar, is just a way of organizing data in a text-based format: each row corresponds to one data entry, with commas in the row separating the values for that entry.

Open up small/people.csv. You’ll see that each person has a unique id, corresponding with their id in IMDb’s database. They also have a name, and a birth year.

Next, open up small/movies.csv. You’ll see here that each movie also has a unique id, in addition to a title and the year in which the movie was released.

Now, open up small/stars.csv. This file establishes a relationship between the people in people.csv and the movies in movies.csv. Each row is a pair of a person_id value and movie_id value. The first row (ignoring the header), for example, states that the person with id 102 starred in the movie with id 104257. Checking that against people.csv and movies.csv, you’ll find that this line is saying that Kevin Bacon starred in the movie “A Few Good Men.”

Next, take a look at degrees.py. At the top, several data structures are defined to store information from the CSV files. The names dictionary is a way to look up a person by their name: it maps names to a set of corresponding ids (because it’s possible that multiple actors have the same name). The people dictionary maps each person’s id to another dictionary with values for the person’s name, birth year, and the set of all the movies they have starred in. And the movies dictionary maps each movie’s id to another dictionary with values for that movie’s title, release year, and the set of all the movie’s stars. The load_data function loads data from the CSV files into these data structures.

The main function in this program first loads data into memory (the directory from which the data is loaded can be specified by a command-line argument). Then, the function prompts the user to type in two names. The person_id_for_name function retrieves the id for any person (and handles prompting the user to clarify, in the event that multiple people have the same name). The function then calls the shortest_path function to compute the shortest path between the two people, and prints out the path.

The shortest_path function, however, is left unimplemented. That’s where you come in!

**Specification**

Complete the implementation of the shortest_path function such that it returns the shortest path from the person with id source to the person with the id target.

Assuming there is a path from the source to the target, your function should return a list, where each list item is the next (movie_id, person_id) pair in the path from the source to the target. Each pair should be a tuple of two strings.

For example, if the return value of shortest_path were [(1, 2), (3, 4)], that would mean that the source starred in movie 1 with person 2, person 2 starred in movie 3 with person 4, and person 4 is the target.

If there are multiple paths of minimum length from the source to the target, your function can return any of them.
If there is no possible path between two actors, your function should return None.

You may call the neighbors_for_person function, which accepts a person’s id as input, and returns a set of (movie_id, person_id) pairs for all people who starred in a movie with a given person.

You should not modify anything else in the file other than the shortest_path function, though you may write additional functions and/or import other Python standard library modules.

**Hints**

While the implementation of search in lecture checks for a goal when a node is popped off the frontier, you can improve the efficiency of your search by checking for a goal as nodes are added to the frontier: if you detect a goal node, no need to add it to the frontier, you can simply return the solution immediately.

You’re welcome to borrow and adapt any code from the lecture examples. We’ve already provided you with a file util.py that contains the lecture implementations for Node, StackFrontier, and QueueFrontier, which you’re welcome to use (and modify if you’d like).



#### 0.2 Tic-Tac-Toe

**Understanding**

There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you’ve completed all the required functions in tictactoe.py, you should be able to run python runner.py to play against your AI!

Let’s open up tictactoe.py to get an understanding for what’s provided. First, we define three variables: X, O, and EMPTY, to represent possible moves of the board.

The function initial_state returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY. What follows are functions that we’ve left up to you to implement!

**Specification**

Complete the implementations of player, actions, result, winner, terminal, utility, and minimax.

The player function should take a board state as input, and return which player’s turn it is (either X or O).

In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.

Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

The actions function should return a set of all of the possible actions that can be taken on a given board.

Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).

Possible moves are any cells on the board that do not already have an X or an O in them.

Any return value is acceptable if a terminal board is provided as input.

The result function takes a board and an action as input, and should return a new board state, without modifying the original board.

If action is not a valid action for the board, your program should raise an exception.

The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.

Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.

The winner function should accept a board as input, and return the winner of the board if there is one.

If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.

One can win the game with three of their moves in a row horizontally, vertically, or diagonally.

You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).

If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.

The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.

If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.

Otherwise, the function should return False if the game is still in progress.

The utility function should accept a terminal board as input and output the utility of the board.

If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.

You may assume utility will only be called on a board if terminal(board) is True.

The minimax function should take a board as input, and return the optimal move for the player to move on that board.

The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.

If the board is a terminal board, the minimax function should return None.

For all functions that accept a board as input, you may assume that it is a valid board (namely, that it is a list that contains three rows, each with three values of either X, O, or EMPTY). You should not modify the function declarations (the order or number of arguments to each function) provided.

Once all functions are implemented correctly, you should be able to run python runner.py and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)

**Hints**

If you’d like to test your functions in a different Python file, you can import them with lines like from tictactoe import initial_state.

You’re welcome to add additional helper functions to tictactoe.py, provided that their names do not collide with function or variable names already in the module.

Alpha-beta pruning is optional, but may make your AI run more efficiently!


