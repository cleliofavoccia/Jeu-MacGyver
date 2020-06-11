
from controller import Controller
from display import Display
from model import Labyrinth

if __name__ == "__main__":
    controller = Controller()
    display = Display()

    #Generate Labyrinth
    controller.labyrinth.generate_labyrinth()

    # Generate items
    controller.generate_items()

    # Display
    controller.view()

    # Game loop
    controller.game_loop()