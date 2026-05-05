"""
Task 1: Set up the project 
Actions: 
• Open VS Code and create a new folder for your project 
• Inside the folder, create a new Python file named adventure_game.py 
• Add an inline comment to describe the purpose of the script 
• Run a simple print statement to confirm that the setup is working
"""
# adventure_game.py
# This script is a text-based adventure game where players explore different locations, make choices, and complete a quest
# to find a legendary treasure.

"""
Task 2: Create a function to start the game 
Actions: 
• Define the function start_game() to display the game introduction 
• Ask the player for their name and store it in a variable 
• Provide the player with an initial choice (explore a forest or enter a cave) 
• Use GitHub Copilot to generate the function body 
"""

from tracemalloc import start


def start_game():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Hello, {name}! Your quest is to find the legendary treasure hidden in this ancient land.")
    print("You have two paths to choose from: a dark forest or a mysterious cave.")
    
    choice = input("Do you want to explore the forest or enter the cave? (forest/cave) ").lower()
    
    if choice == "forest":
        forest_path()
    elif choice == "cave":
        cave_path()
    else:
        print("Invalid choice. Please choose 'forest' or 'cave'.")
        start_game()  # Restart the game if an invalid choice is made

"""
Task 3: Create the forest path 
Actions: 
• Define the function forest_path() that describes the forest scenario 
• Provide the player with choices (follow a river or climb a tree) 
• Use an if-else structure to handle player choices 
"""

def forest_path():
    print("You venture into the dark forest. The trees are tall and the atmosphere is eerie.")
    print("You see a river flowing nearby and a tree that looks climbable.")
    
    choice = input("Do you want to follow the river or climb the tree? (river/tree) ").lower()
    
    if choice == "river":
        print("You follow the river and find a hidden path that leads you to a waterfall. There is a chest at the bottom of the falls! Could it be the treasure?")
        yes_no = input("Do you want to investigate the chest? (yes/no) ").lower()
        if yes_no == "yes":
            dive_climb = input("Should you dive into the water or climb down the cliff to reach the chest? (dive/climb) ").lower()
            if dive_climb == "dive":
                print("You dive into the water and swim towards the chest. As you reach it, you find a hidden compartment with a key inside!")
            elif dive_climb == "climb":
                print("The rocks are slippering, you fall and must start over!")
                start_game()  # Restart the game if an invalid choice is made`   
        elif yes_no == "no":
            print("You deside to head back to the beginning of the path and climb the tree!")
            choice = "tree"
    elif choice == "tree":
        print("You climb the tree and get a better view of the surroundings. You spot something shiny in the distance!")
        # Continue the adventure...
    else:
        print("Invalid choice. Please choose 'river' or 'tree'.")
        forest_path()  # Restart the forest path if an invalid choice is made

"""
Task 4: Create the cave path 
Actions: 
• Define the function cave_path() that describes the cave scenario 
• Provide the player with choices (light a torch or proceed in the dark) 
• Use conditionals to determine the outcome 
"""

def cave_path():
    print("You enter the mysterious cave. It's dark and you can hear dripping water.")
    print("You have a torch with you, but you can also choose to proceed in the dark.")
    
    choice = input("Do you want to light the torch or proceed in the dark? (torch/dark) ").lower()
    
    if choice == "torch":
        print("You light the torch and see a hidden passage that leads you deeper into the cave!")
        # Continue the adventure...
    elif choice == "dark":
        print("You proceed in the dark and stumble upon a hidden trap! You lose your way and have to start over.")
        start_game()  # Restart the game if the player chooses to proceed in the dark
    else:
        print("Invalid choice. Please choose 'torch' or 'dark'.")
        cave_path()  # Restart the cave path if an invalid choice is made

"""
Task 5: Run the adventure game 
Actions: 
• Call start_game() to begin the adventure 
• Ensure the program runs in a loop until the player completes their journey 
• Provide an option to restart the game after completion 
"""

if __name__ == "__main__":
    start_game()    