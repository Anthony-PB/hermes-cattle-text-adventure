import time
import sys
import readchar

def typewriter(text, delay=0.03):
    """Prints text character-by-character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_choice(valid_choices=['A', 'B']):
    """Waits for a specific key press (A, B, C, ...)."""
    while True:
        key = readchar.readkey().upper()
        if key in valid_choices:
            print(f"> {key}")
            return key

class GameState:
    def __init__(self):
        self.motif_points = 0
        self.inventory = []

    def add_motif(self, reason):
        self.motif_points += 1
        print(f"\n[+1 MOTIF: {reason}]")
        time.sleep(1)

def stage_1_birth(state):
    typewriter("\n--- STAGE 1: THE CAVE ---")
    typewriter("You are Hermes. Born at dawn. Hungry by noon.")
    typewriter("You stand at the mouth of the cave. A tortoise waddles by.")
    
    print("\nA. Ignore it and go back to sleep.")
    print("B. Catch it (Invention of the Lyre).")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        typewriter("You go back to sleep. You remain a minor deity forever.")
        return False # Game Over
    else:
        typewriter("You scoop out the shell and stretch cowhide over it.")
        typewriter("You have invented the LYRE. The world is full of music.")
        state.add_motif("Invention (Techne)")
        state.inventory.append("Lyre")
        return True # Continue

def stage_2_cattle(state):
    typewriter("\n--- STAGE 2: THEFT IN PIERIA ---")
    typewriter("Night falls. You find Apollo's sacred cattle.")
    typewriter("Objective: Steal them without getting caught.")

    print("\nA. Drive them normally (Fast).")
    print("B. Drive them backward to reverse the tracks (Cunning).")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        typewriter("Apollo follows the tracks. You are caught immediately.")
        return False
    else:
        typewriter("Clever! The tracks look like the cows are walking TOWARDS the meadow.")
        typewriter("You hide the cows in a cave by the river Alpheus.")
        state.add_motif("Trickster/Thief")
        return True

def stage_3_trial(state):
    typewriter("\n--- STAGE 3: THE TRIAL ---")
    typewriter("Apollo drags you to Olympus before Zeus.")
    typewriter("He knows you stole the cows, but he has no proof.")
    
    print("\nA. Fight Apollo.")
    print("B. Deny everything, then trade the Lyre for peace.")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        typewriter("You are a baby. Apollo pummels you.")
        return False
    else:
        typewriter("You play the Lyre. Apollo is enchanted by the music.")
        typewriter("He lets you keep the cows in exchange for the instrument.")
        state.add_motif("Reconciliation/Exchange")
        return True

def main():
    state = GameState()
    
    # Title Screen
    print("\n" + "="*30)
    print("      PROJECT MAIA")
    print("="*30)
    time.sleep(1)

    # Execute Stages
    if stage_1_birth(state):
        if stage_2_cattle(state):
            if stage_3_trial(state):
                # Victory Screen
                print("\n" + "="*30)
                print(f"VICTORY! Final Score: {state.motif_points}/3")
                print("You have earned your place on Olympus.")
                print("="*30)
                return

    # Game Over Screen
    print("\n[GAME OVER]")
    print("Try again to earn your glory (kleos).")

if __name__ == "__main__":
    main()