"""
Task 1: Set up the project 
Actions: 
• Open VS Code and create a new folder for your project 
• Inside the folder, create a new Python file named adventure_game.py 
• Add an inline comment to describe the purpose of the script 
• Run a simple print statement to confirm that the setup is working
"""

"""
Task 2: Create a function to start the game 
Actions: 
• Define the function start_game() to display the game introduction 
• Ask the player for their name and store it in a variable 
• Provide the player with an initial choice (explore a forest or enter a cave) 
• Use GitHub Copilot to generate the function body 
"""

def start_game():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Hello, {name}! Your adventure begins now.")
    choice = input("Do you want to explore the forest or enter the cave? (forest/cave) ")
    if choice.lower() == "forest":
        print("You venture into the mysterious forest, surrounded by towering trees and the sounds of wildlife.")
    elif choice.lower() == "cave":
        print("You step into the dark cave, feeling the cool air and hearing the echoes of dripping water.")
    else:
        print("Invalid choice. Please choose 'forest' or 'cave'.")