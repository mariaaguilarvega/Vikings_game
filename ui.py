import os
import readchar


class UI():

    @staticmethod
    def clear():
        """Clear the terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def ask_for_int(msg):
        while True:
            try:
                response = int(input(msg))
                return response
            except ValueError:
                UI.clear()
                print("Please enter a valid number")

    @staticmethod
    def display_user_menu(options, intro = ""):
        """Display some options for the user to choose, and return the index of the option selected"""
        selected = 0

        while True:
            UI.clear()

            # display intro message
            print("\n\n")
            print(intro)
            print("\n")

            # display all available options
            for i, option in enumerate(options):
                prefix = "→ " if i == selected else "  "
                print(f"{prefix}{option}")
            
            # get user's choice
            key = readchar.readkey()
            if key == readchar.key.UP and selected > 0:
                selected -= 1
            elif key == readchar.key.DOWN and selected < len(options) - 1:
                selected += 1
            elif key == readchar.key.ENTER:
                break
        
        UI.clear()
        return selected

    @staticmethod
    def display_message(msg = ""):
        """Display a message, and wait for user confirmation"""
        UI.display_user_menu(["Ok!"], msg)


