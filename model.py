"""Creation of models which will be used
to create objects in controller.py"""


class MacGyver:
    """Attributes and methods (move, drop items) of object type MacGyver"""
    def __init__(self, case_y, case_x, mac_image):
        """Attributes of MacGyver : inventory,
        position in labyrinth list (case_y, case_x)
        and his image"""
        self.inventory = []
        self.case_y = case_y
        self.case_x = case_x
        self.mac_image = mac_image

    def move_right(self):
        """MacGyver movement to the right case"""
        self.case_x = self.case_x + 1

    def move_left(self):
        """MacGyver movement to the left case"""
        self.case_x = self.case_x - 1

    def move_up(self):
        """MacGyver movement to the up case"""
        self.case_y = self.case_y - 1

    def move_down(self):
        """MacGyver movement to the down case"""
        self.case_y = self.case_y + 1

    def add_items(self):
        """Drop items to inventory"""
        self.inventory.append('')


class Guardian:
    """Attributes of object type Guardian.
    It has no method because it's static object."""
    def __init__(self, case_y, case_x, guard_image):
        """Attributes of Guardian :
        position in labyrinth list (case_y, case_x)
        and his image"""
        self.case_y = case_y
        self.case_x = case_x
        self.guard_image = guard_image


class Item:
    """Attributes of object type Item.
    It has no method because it's static object."""
    def __init__(self, case_y, case_x, image):
        """Attributes of Item :
        position in labyrinth list (case_y, case_x)
        and his image"""
        self.case_y = case_y
        self.case_x = case_x
        self.image = image


class Labyrinth:
    """Attributes and method (generate) of object type Labyrinth"""
    def __init__(self, wall_image, floor_image):
        """Attributes of Labyrinth :
        floor and wall image
        and initialization of labyrinth list"""
        self.wall_image = wall_image
        self.floor_image = floor_image
        self.lab = []

    def generate_labyrinth(self):
        """Generation of labyrinth list from
        'labyrinth.txt' file to self.lab list"""
        # Open the file labyrinth.txt
        with open('labyrinth.txt', "r") as labyrinth:
            # Browse the lines in labyrinth.txt
            for line in labyrinth:
                lines = []
                # Browse the characters in labyrinth.txt
                for char in line:
                    # Print error if characters is not
                    # '0', '1' or line break
                    if char not in ('0', '1', "\n"):
                        print("Error")
                    elif char != "\n":
                        # Add characters in lab list
                        lines.append(char)
                self.lab.append(lines)
