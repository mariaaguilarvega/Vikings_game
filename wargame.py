import sys
import pygame

from data.battles import battles
from ui import UI
from game_classes import War



def main():

    UI.clear()

    # Allow the user to choose a battle
    battle_names = [battle["battle_name"] for battle in battles]
    battle_index = UI.display_user_menu(battle_names, "Choose a battle:")
    battle_data = battles[battle_index]

    UI.clear()

    # Get player names
    player_1 = input("Player 1, write your name: ")
    player_2 = input("Player 2, write your name: ")

    try:

        # Initialize music
        pygame.mixer.init()
        pygame.mixer.music.load('fight.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # Start the battle
        great_war = War(player_1, player_2, battle_data)
        great_war.start()

        sys.exit()

    except KeyboardInterrupt:
        UI.display_message("Game interrupted by the user")
        sys.exit()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
    
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    main()

