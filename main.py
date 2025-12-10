import time
import sys
import random
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
        if random.random() > 0.4:
            typewriter("You close your eyes, drifting off...")
            time.sleep(1)
            typewriter("...CLUNK.")
            typewriter("The clumsy tortoise knocks over a clay pot next to your head.")
            typewriter("You wake up startled! The tortoise scurries away.")
            typewriter("You are awake now, but you missed the chance to make the Lyre.")
            return True # Continue
        else:
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
        return True # Continue
    else:
        if random.random() > 0.5:
            typewriter("You try to herd the entire massive herd. It's chaos.")
            typewriter("BUT... Zeus looks down from Olympus and chuckles.")
            typewriter("'This child has ambition!' he laughs.")
            typewriter("He sends a mist to cover your escape. You manage to get away.")
            return True # Continue
        else:
            typewriter("The gods notice your greed. You are too loud.")
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
        if random.random() > 0.5:
            typewriter("You leave massive footprints leading right to your cave.")
            typewriter("Apollo is flying overhead...")
            typewriter("SUDDENLY! A freak windstorm sweeps across the road.")
            typewriter("The sand covers your tracks just in time.")
            typewriter("You got lucky. Very lucky.")
            return True # Continue
        else:
            typewriter("Apollo follows the tracks. You are caught immediately.")
            return False # Game Over
    else:
        typewriter("Clever! The tracks look like the cows are walking TOWARDS the meadow.")
        typewriter("You have gained a valuable thing, time.")
        typewriter("Apollo is temporarily confused.")
        state.add_motif("Trickster/Thief")
        return True # Continue
    
def stage_4_hide(state):
    typewriter("\n--- STAGE 4: THE HIDING SPOT & SACRIFICE ---")
    typewriter("You arrive at the River Alpheus with the herd.")
    typewriter("You sacrifice 2 cows to the 12 Gods (audaciously including yourself).")
    typewriter("The smell of roasting meat is overwhelming. You are starving.")
    
    print("\nA. Eat the meat (satisfy your hunger).")
    print("B. Resist the hunger, hide the rest in a cave, and run home.")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        if random.random() > 0.3:
            typewriter("You bite into the steak...")
            time.sleep(1)
            typewriter("...and immediately spit it out!")
            typewriter("Your divine body REJECTS mortal flesh.")
            typewriter("Gods consume only ambrosia and smoke.")
            typewriter("You are still hungry, but you didn't ruin your divinity.")
            return True # Continue
        else:
            typewriter("You eat the meat. You give in to mortal hunger.")
            typewriter("You fall asleep by the river with grease on your chin.")
            typewriter("Apollo catches you red-handed.")
            return False # Game Over
    else:
        typewriter("Success! You prove your divinity by resisting the meat.")
        typewriter("You stash the remaining 48 cows in a cave.")
        typewriter("You fly back to your mother's cave and wrap yourself in blankets.")
        typewriter("Just in time. Apollo is coming.")
        state.add_motif("Sacrifice/Alibi")
        return True # Continue

def stage_5_trial(state):
    typewriter("\n--- STAGE 5: THE TRIAL ---")
    typewriter("Apollo drags you to Olympus before Zeus.")
    typewriter("He knows you stole the cows, but he has no proof.")
    
    print("\nA. Fight Apollo.")
    print("B. Deny everything, then trade the Lyre for peace.")

    choice = get_choice(['A', 'B'])

    if choice == 'A':
        if random.random() > 0.45:
            typewriter("You clench your baby fists and swing at the Sun God.")
            typewriter("Zeus roars with laughter from his throne.")
            typewriter("'ENOUGH!' he bellows, wiping a tear from his eye.")
            typewriter("'I haven't laughed this hard in eons. No fighting.'")
            typewriter("He forces Apollo to put you down. You survived.")
            return True # Continue
        else:
            typewriter("You are a baby. Apollo pummels you.")
            return False # Game Over
    else:
        if "Lyre" in state.inventory:
            typewriter("You play the Lyre. Apollo is enchanted by the music.")
            typewriter("He lets you keep the cows in exchange for the instrument.")
            state.add_motif("Reconciliation/Exchange")
            return True # Continue
        else:
            typewriter("You try to trade... but you have nothing to give him!")
            typewriter("You missed the tortoise earlier.")
            typewriter("Apollo takes his cows back, but Zeus finds your audacity funny.")
            typewriter("You survive, but you gain no glory.")
            return True # Continue

def main():
    try:
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
                            if(state.motif_points > 3):
                                print("\n" + "="*30)
                                print(f"VICTORY! Final Score: {state.motif_points}/5")
                                print("You have earned your place on Olympus.")
                                print("="*30)
                                input("\nPress Enter to exit...")
                                return
                            else:
                                typewriter("\n")
                                typewriter("You are lucky to have gotten this far.")
                                typewriter("BUT, this is where your story ends.")
                                typewriter("You did not display enough Metis (Cunning).")
                                typewriter(f"Final Score: {state.motif_points}/5 (Mediocre)")
    except KeyboardInterrupt:
        print("\n")
        print("-"*30)
        print("*"*5 + " Exited Forcefully. " + "*"*5)
        print("-"*30)
        return
    except Exception as e:
        print("Critical Error. Sorry!")
        print(e)

    # Game Over Screen
    print("\n[GAME OVER]")
    print("Try again to earn your glory (kleos).")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()