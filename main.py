import time
import sys
try:
    import readchar
except ImportError:
    print("\n" + "!"*50)
    print("MISSING DEPENDENCY ERROR")
    print("!"*50)
    print("This game requires the 'readchar' library to detect keystrokes.")
    print("Please run the following command in your terminal:")
    print("\n    pip install readchar\n")
    print("Then run the game again.")
    print("!"*50 + "\n")
    input("Press Enter to exit...")
    sys.exit()

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
    typewriter("\n--- STAGE 1: BIRTH ---")
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

    print("\nA. Steal 50 cows.")
    print("B. Steal all of the cows.")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        typewriter("What a good, nice, and round number. Very sneaky.")
        state.add_motif("Trickster/Thief")
        return True
    else:
        typewriter("The gods notice your greed.")
        return False # Game Over

def stage_3_travel(state):
    typewriter("\n--- STAGE 3: TRAVELING WITH THE CATTLE ---")
    typewriter("You are driving the herd from Pieria to Pylos.") 
    typewriter("The road is long and sandy.")
    typewriter("Objective: Hide your tracks from Apollo.")

    print("\nA. Drive them normally.")
    print("B. Drive them backward to reverse the tracks.")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        typewriter("Apollo follows the tracks. You are caught immediately.")
        return False
    else:
        typewriter("Clever! The tracks look like the cows are walking TOWARDS the meadow.")
        typewriter("You have gained a valuable thing, time.")
        typewriter("Apollo is temporarily confused.")
        state.add_motif("Trickster/Thief")
        return True
    
def stage_4_hide(state):
    typewriter("\n--- STAGE 4: THE HIDING SPOT & SACRIFICE ---")
    typewriter("You arrive at the River Alpheus with the herd.")
    typewriter("You sacrifice 2 cows to the 12 Gods (audaciously including yourself).")
    typewriter("The smell of roasting meat is overwhelming. You are starving.")
    
    print("\nA. Eat the meat (satisfy your hunger).")
    print("B. Resist the hunger, hide the rest in a cave, and run home.")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        typewriter("You eat the meat. Gods feast on smoke, only mortals eat flesh.")
        typewriter("You fall asleep by the river with grease on your chin.")
        typewriter("Apollo catches you red-handed.")
        return False # Game Over
    else:
        typewriter("Success! You prove your divinity by resisting the meat.")
        typewriter("You stash the remaining 48 cows in a cave.")
        typewriter("You fly back to your mother's cave and wrap yourself in blankets.")
        typewriter("Just in time. Apollo is coming.")
        state.add_motif("Sacrifice/Alibi")
        return True

def stage_5_trial(state):
    typewriter("\n--- STAGE 5: THE TRIAL ---")
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
    print("Tip: Ensure sound is on (metaphorically).")
    time.sleep(1)

    # Execute Stages
    if stage_1_birth(state):
        if stage_2_cattle(state):
            if stage_3_travel(state):
                if stage_4_hide(state):
                    if stage_5_trial(state):
                        # Victory Screen
                        print("\n" + "="*30)
                        print(f"VICTORY! Final Score: {state.motif_points}/5")
                        print("You have earned your place on Olympus.")
                        print("="*30)
                        input("\nPress Enter to exit...")
                        return

    # Game Over Screen
    print("\n[GAME OVER]")
    print("Try again to earn your glory (kleos).")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()