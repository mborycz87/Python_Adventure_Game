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
affects_choices = set()

def start_game():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Hello, {name}! Your quest is to find the Treasure of Tarshish.")
    print("To find the treasure, you will need to explore different locations, solve puzzles, and make important choices along the way.")
    print("Before you begin you see an ingraving on a rock, a poem, a clue!!!")
    print("The treasure of Tarshish was hidden by three.")
    print("These three could hide in places better than a tree.")
    print("One was thirsty, one loved puzzles, and the third would say anything for a modest fee.")
    print("After you read the peom, you have two paths to choose from: a dark forest or a mysterious cave.")
    
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
        if "river_key" in affects_choices:
            print("You already have the key from the water fall, so you decide to head back to the tree and climb it instead!")
            tree_path()  # Continue to the tree path if the player already has the key
        else:
            print("You follow the river and find a hidden path that leads you to a waterfall. There is a chest at the bottom of the falls! Could it be the treasure?")
            yes_no = input("Do you want to investigate the chest? (yes/no) ").lower()
            if yes_no == "yes":
                dive_climb = input("Should you dive into the water or climb down the cliff to reach the chest? (dive/climb) ").lower()
                if dive_climb == "dive":
                    print("You dive into the water and swim towards the chest. As you reach it, you find a hidden compartment with a key inside!")
                    print("Although you found the key, you realize that the chest is empty. You need to find the lock that this key opens!")
                    affects_choices.add("river_key")  # Add the key to the player's inventory
                    print("\nYou now have the River Key (from the thirsty one)!")
                    choice = input("Would you like to continue exploring the river or head back to the tree? (river/tree) ").lower()
                    if choice == "tree":
                        tree_path()
                    else:
                        forest_path()
                elif dive_climb == "climb":
                    print("The rocks are slippering, you fall and must start over!")
                    start_game()  # Restart the game if an invalid choice is made
            elif yes_no == "no":
                print("You deside to head back to the beginning of the path and climb the tree!")
                tree_path()  # Continue to the tree path if the player chooses not to investigate the chest
    elif choice == "tree":
        tree_path()
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
        puzzle_chamber()
    elif choice == "dark":
        print("You proceed in the dark and stumble upon a hidden trap! You lose your way and have to start over.")
        start_game()  # Restart the game if the player chooses to proceed in the dark
    else:
        print("Invalid choice. Please choose 'torch' or 'dark'.")
        cave_path()  # Restart the cave path if an invalid choice is made

"""
Puzzle Chamber - Where players solve a riddle to get the puzzle key
"""

def puzzle_chamber():
    if "puzzle_key" in affects_choices:
        print("You've already solved the puzzle here. The riddle is satisfied.")
        check_for_treasure()
        return
    
    print("\nYou venture deeper into the cave and discover a grand chamber.")
    print("The walls are covered in ancient writings. A stone pedestal stands in the center with an inscription:")
    print("\n'I am the largest land creature that roams. I have big ears and a long trunk for home.'")
    print("'Answer correctly and claim the key that unlocks the secrets of the hidden treasure.'")
    
    attempts = 3
    while attempts > 0:
        answer = input("\nWhat is the answer? ").lower().strip()
        
        if answer == "elephant":
            print("\nCorrect! The pedestal glows with ancient magic and a key emerges!")
            print("You have found the Puzzle Key (from the one who loved puzzles)!")
            affects_choices.add("puzzle_key")
            check_for_treasure()
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect. Try again. You have {attempts} attempt(s) left.")
                if attempts == 1:
                    print("Hint: It's a large grey animal found in Africa and Asia.")
            else:
                print("You've run out of attempts. The chamber collapses around you!")
                print("You must start your adventure over...")
                start_game()
                return

"""
Tree Path - Where players find a coin to trade for the fee key
"""

def tree_path():
    print("You climb the tree and get a better view of the surroundings. You spot something shiny in the distance!")
    choice = input("Do you want to investigate the shiny object? (yes/no) ").lower()
    
    if choice == "yes":
        print("After a long winding and twisting path, you come across the object embedded in a stone. It's an ancient coin!")
        print("What did that poem say about a 'fee'?")
        affects_choices.add("fee_coin")
        print("\nYou now have the Ancient Coin!")
        merchant_encounter()
    elif choice == "no":
        print("You decide to head back to the beginning of the path and explore the river instead!")
        forest_path()  # Continue to the river path if the player chooses not to investigate the shiny object
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        tree_path()  # Restart the tree path if an invalid choice is made

"""
Merchant Encounter - Where players trade the coin for the fee key
"""

def merchant_encounter():
    if "fee_key" in affects_choices:
        print("The merchant has already given you the fee key.")
        check_for_treasure()
        return
    
    if "fee_coin" not in affects_choices:
        print("You don't have anything the merchant wants.")
        return
    
    print("\n" + "="*60)
    print("As you examine the coin, a figure emerges from the shadows.")
    print("An old merchant with a knowing smile appears before you.")
    print("'Ah, I see you have found the ancient coin,' he says.")
    print("'I have been expecting someone. That coin is worth a great price.'")
    print("'I will trade you a key for it. A key that opens the lock to the treasure.'")
    print("="*60)
    
    trade_choice = input("\nDo you want to trade the coin for the key? (yes/no) ").lower()
    
    if trade_choice == "yes":
        print("\nThe merchant takes the coin and hands you a mysterious key.")
        print("'The treasure is yours to claim,' he whispers, then fades into the darkness.")
        print("You have found the Fee Key (from the one who wanted payment)!")
        affects_choices.add("fee_key")
        check_for_treasure()
    elif trade_choice == "no":
        print("The merchant nods and disappears. The coin remains in your possession.")
        print("Perhaps you'll find another use for it...")
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        merchant_encounter()

"""
Check for Treasure - Determines if player has all three keys to unlock the treasure
"""

def check_for_treasure():
    print("\n" + "="*60)
    print("CURRENT KEYS COLLECTED:")
    print(f"  River Key (Thirsty One): {'✓' if 'river_key' in affects_choices else '✗'}")
    print(f"  Puzzle Key (Puzzle Lover): {'✓' if 'puzzle_key' in affects_choices else '✗'}")
    print(f"  Fee Key (Greedy One): {'✓' if 'fee_key' in affects_choices else '✗'}")
    print("="*60 + "\n")
    
    required_keys = {"river_key", "puzzle_key", "fee_key"}
    
    if required_keys.issubset(affects_choices):
        unlock_treasure()
    else:
        missing_count = len(required_keys - affects_choices)
        print(f"You still need {missing_count} more key(s) to unlock the treasure.")
        print("Continue your adventure to find the remaining keys!\n")
        
        next_choice = input("What would you like to do? (forest/cave/check) ").lower()
        if next_choice == "forest":
            forest_path()
        elif next_choice == "cave":
            cave_path()
        elif next_choice == "check":
            check_for_treasure()
        else:
            print("Invalid choice.")
            check_for_treasure()

"""
Unlock Treasure - The final scene when player has all three keys
"""

def unlock_treasure():
    print("\n" + "🎉" * 30)
    print("\nYOU HAVE FOUND ALL THREE KEYS!\n")
    print("The ground beneath you begins to tremble. The ancient magic awakens!")
    print("Before you, a magnificent door materializes, covered in three ornate keyholes.")
    print("\nWith trembling hands, you insert the River Key...")
    print("  → A deep rumble echoes through the chamber.")
    print("\nYou insert the Puzzle Key...")
    print("  → Golden light begins to shine from the cracks in the door.")
    print("\nFinally, you insert the Fee Key...")
    print("  → The door swings open with a brilliant flash of light!")
    print("\n" + "="*60)
    print("INSIDE THE TREASURE CHAMBER")
    print("="*60)
    print("\nBefore you lies the legendary Treasure of Tarshish!")
    print("Piles of gold coins, jewels, ancient artifacts, and treasures beyond imagination.")
    print("Your quest is complete!")
    print("\n🎊 CONGRATULATIONS! YOU HAVE WON THE GAME! 🎊\n")
    print("🎉" * 30)
    
    play_again = input("\nWould you like to play again? (yes/no) ").lower()
    if play_again == "yes":
        affects_choices.clear()  # Reset the game
        start_game()
    else:
        print("Thank you for playing the Adventure Game! Goodbye!")

"""
Task 5: Run the adventure game 
Actions: 
• Call start_game() to begin the adventure 
• Ensure the program runs in a loop until the player completes their journey 
• Provide an option to restart the game after completion 
"""

if __name__ == "__main__":
    start_game()
