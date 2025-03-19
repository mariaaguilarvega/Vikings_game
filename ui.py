import os
import readchar
import sys


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
    def display_user_menu(options, intro=""):
        selected = 0

        # Print the initial menu
        print("\n" + intro + "\n")
        for i, option in enumerate(options):
            prefix = "→ " if i == selected else "  "
            print(f"{prefix}{option}")

        while True:
            sys.stdout.write("\033[F" * len(options))  # Move cursor up to redraw only the menu
            for i, option in enumerate(options):
                prefix = "→ " if i == selected else "  "
                print(f"{prefix}{option}")

            key = readchar.readkey()
            if key == readchar.key.UP and selected > 0:
                selected -= 1
            elif key == readchar.key.DOWN and selected < len(options) - 1:
                selected += 1
            elif key == readchar.key.ENTER:
                break

        return selected

    @staticmethod
    def display_message(msg = ""):
        """Display a message, and wait for user confirmation"""
        UI.display_user_menu(["Game-over!"], msg)


