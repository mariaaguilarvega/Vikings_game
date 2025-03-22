import sys
import pygame

from data.battles import battles
from ui import UI
from game_classes import War



def main():

    AUDIO_PATH = "audio/"

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
        pygame.mixer.music.load(f"{AUDIO_PATH}fight.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # Start the battle
        great_war = War(player_1, player_2, battle_data)
        winner = great_war.start()

        # Get data from the winning army
        if winner == 1:
            winning_army_name = battle_data["army_1"]["army_name"]
            winning_army_theme = battle_data["army_1"].get("theme", {})
        elif winner == 2:
            winning_army_name = battle_data["army_2"]["army_name"]
            winning_army_theme = battle_data["army_2"].get("theme", {})

        # Get the theme music for the winning army
        winner_theme_file = winning_army_theme.get("filename", None)
        winner_theme_start = winning_army_theme.get("start_at", 0.0)

        # Play the theme music for the winning army
        if winner_theme_file:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f"{AUDIO_PATH}{winner_theme_file}")
            pygame.mixer.music.play(start=winner_theme_start)
            
        UI.display_message(f"{winning_army_name} have won the battle of the century!", "Game Over!")
        UI.clear()
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

