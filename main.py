"""Execute the game"""
from controller import Controller

if __name__ == "__main__":
    """Call of methods view and game_loop
    from Controller class to execute the game"""
    controller = Controller()

    # Display
    controller.view()

    # Game loop
    controller.game_loop()
