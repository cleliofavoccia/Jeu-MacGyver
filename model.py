import os

class MacGyver:
    def __init__(self, case_y, case_x, mac_image):
        # inventory
        self.inventory = []
        # position list
        self.case_y = case_y
        self.case_x = case_x
        # image
        self.mac_image = mac_image

    def move_right(self):
        self.case_x = self.case_x + 1

    def move_left(self):
        self.case_x = self.case_x - 1

    def move_up(self):
        self.case_y = self.case_y - 1

    def move_down(self):
        self.case_y = self.case_y + 1

    # drop items to inventory
    def add_items(self, item):
        self.inventory.append(item)


class Guardian:
    def __init__(self, case_y, case_x, guard_image):
        # position list
        self.case_y = case_y
        self.case_x = case_x
        # image
        self.guard_image = guard_image

class Item:
    def __init__(self, case_y, case_x, image):
        self.case_y = case_y
        self.case_x = case_x
        self.image = image
        self.is_collected = False

class Labyrinth:

    def __init__(self, wall_image, floor_image):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'labyrinth.txt')
        # image
        self.wall_image = wall_image
        self.floor_image = floor_image
        #initialization labyrinth list
        self.lab = []

    #generation labyrinth list
    def generate_labyrinth(self):
        with open('labyrinth.txt', "r") as labyrinth:
            for line in labyrinth:
                lign = []
                for char in line:
                    if char != '0' and char != '1' and char != "\n":
                        print("error")
                    elif char != "\n":
                        lign.append(char)
                self.lab.append(lign)


#
#
#
# if __name__ == "__main__":
#     laby = Labyrinth("ss.png", "aa.png")
#     laby.generate_labyrinth()
#     print(laby.floor_list)
#     # print (laby.floor_list[14][0])



