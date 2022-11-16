# defines a series of functions for generating or manipulating random integers
import random
# parameter and function access
import sys


# a code template for creating objects
# A class in Python is a category or set of different elements grouped together that share one or more similarities with one another, but yet distinct from other classes via type, quality and kind. In technical terminology, we can define a class in Python as being a blueprint for individual objects with same or exact behavior.
class Computer_Move:
    # if variable_1 is set to anything non-empty, then use its value, otherwise use 0
    rows = 0
    cols = 0
    computer_primary_arr = []
    computer_tracking_arr = []
    computer_ship_name = []
    ships = []
    used_spaces = []
    count_B = 4
    count_Carrier = 5
    count_Cruiser = 3
    count_S = 4
    count_D = 2
    input = {}
    #letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # The self in keyword in Python is used to all the instances in a class. By using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes.
    # _init_ it is known as a constructor. The __init__ method can be called when an object is created from the class, and access is required to initialize the attributes of the class.
    def __init__(self):
        self.rows = h.rows
        self.cols = h.cols
        self.computer_primary_arr = [['.' for x in range(self.cols)] for y in range(self.rows)]
        self.computer_tracking_arr = [['.' for x in range(self.cols)] for y in range(self.rows)]
        self.ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

    # define where the computer will place the ship
    def Computer_Place_Ship(self):
        if (len(self.ships) == 0):
            h.play()
        else:
            count = 0
            possibilities = []
            # Ship Name
            ship = self.ships.pop(self.ships.index(random.choice(self.ships))).lower()
            self.computer_ship_name.append(ship.lower())

            choice = random.randint(1, 2)

            if choice == 1:

                computer_ship_start_letter = random.randint(1, self.cols)

                computer_ship_end_letter = computer_ship_start_letter

                if self.computer_ship_name[-1] == "carrier":
                    ship_letter = "C"
                    difference = 5
                elif self.computer_ship_name[-1] == "battleship":
                    ship_letter = "B"
                    difference = 4
                elif self.computer_ship_name[-1] == "cruiser":
                    ship_letter = "C"
                    difference = 3
                elif self.computer_ship_name[-1] == "submarine":
                    ship_letter = "S"
                    difference = 3
                elif self.computer_ship_name[-1] == "destroyer":
                    ship_letter = "D"
                    difference = 2

                difference = difference - 1
                computer_ship_start_number = random.randint(1, self.rows - difference)
                computer_ship_end_number = computer_ship_start_number + difference


                # Letter (If letter is same and number is different)
                #TODO:
                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                letter = letters[random.randint(0,self.cols-1)]   #chr(ord(str(computer_ship_start_letter - 1)) + 17)
                # All Possibilities
                for i in range(computer_ship_start_number, computer_ship_end_number + 1):
                    points = str(letter) + str(i)
                    possibilities.append(points)
                    if points in self.used_spaces:
                        count = count + 1  # If anything is append in this iteration
            else:
                computer_ship_start_number = random.randint(1, self.rows)
                computer_ship_end_number = computer_ship_start_number

                if self.computer_ship_name[-1] == "carrier":
                    ship_letter = "C"
                    difference = 5
                # elseif
                elif self.computer_ship_name[-1] == "battleship":
                    ship_letter = "B"
                    difference = 4
                elif self.computer_ship_name[-1] == "cruiser":
                    ship_letter = "C"
                    difference = 3
                elif self.computer_ship_name[-1] == "submarine":
                    ship_letter = "S"
                    difference = 3
                elif self.computer_ship_name[-1] == "destroyer":
                    ship_letter = "D"
                    difference = 2

                # Decrement Because of range function
                difference = difference - 1
                computer_ship_start_letter = random.randint(1, self.cols - difference)
                computer_ship_end_letter = computer_ship_start_letter + difference


                # All Possibilities (If Number is same and letter is different)
                #TODO:
                letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                for i in range(computer_ship_start_letter, computer_ship_end_letter + 1):
                    letter = letters[i-1]   #chr(ord(str(i - 1)) + 17)
                    points = str(letter) + str(computer_ship_start_number)
                    possibilities.append(points)
                    if points in self.used_spaces:
                        count = count + 1

            # computer_starting_point = chr(ord(str(computer_ship_start_letter - 1)) + 17) + str(computer_ship_start_number - 1)
            #computer_ending_point = chr(ord(str(computer_ship_end_letter - 1)) + 17) + str(computer_ship_end_number - 1)
            computer_starting_point = letters[computer_ship_start_letter].upper()+str(computer_ship_start_number - 1)
            computer_ending_point = letters[computer_ship_end_letter].upper()+str(computer_ship_end_number-1)
            self.input[self.computer_ship_name[-1]] = computer_starting_point, computer_ending_point

            if count == 0:
                # If nothing overlaps then append in used spaces and use placement function
                for i in possibilities:
                    self.used_spaces.append(i)

                self.Placement(computer_ship_start_letter, computer_ship_start_number, computer_ship_end_letter,
                               computer_ship_end_number, ship_letter)

            else:
                self.ships.append(ship)
                self.Computer_Place_Ship()

    def Placement(self, computer_ship_start_letter, computer_ship_start_number, computer_ship_end_letter,
                  computer_ship_end_number, ship_letter):

        for i in range(computer_ship_start_number - 1, computer_ship_end_number):
            for j in range(computer_ship_start_letter - 1, computer_ship_end_letter):
                if self.computer_primary_arr[i][j] == ".":
                    self.computer_primary_arr[i][j] = ship_letter

        self.Computer_Place_Ship()

    def Computer_Guess(self):
        print("Computer Guess : ")
        int_computer_guess_letter = random.randint(1, self.cols)
        computer_guess_number = random.randint(1, self.rows)
        computer_guess_letter = chr(int_computer_guess_letter + 96)

    def Computer_Guess(self):
        print("Computer Guesses : ", end="")

        computer_guess_letter = random.randint(0, self.cols - 1)
        computer_guess_number = random.randint(1, self.rows)
        computer_guess = chr(ord(str(computer_guess_letter)) + 17) + str(computer_guess_number)
        print(computer_guess)

        file = open("Summary_Log", 'a')
        file.write("\nComputer Guess : " + computer_guess)
        file.close()

        # -1 because rows starts from 0
        if h.primary_arr[computer_guess_number - 1][computer_guess_letter] == ".":
            print("Miss!")
            self.computer_tracking_arr[computer_guess_number - 1][computer_guess_letter] = "M"
            h.Guess()
        else:
            print("Hit!")
            self.computer_tracking_arr[computer_guess_number - 1][computer_guess_letter] = "X"
            letter = h.primary_arr[computer_guess_number - 1][computer_guess_letter]

            if letter == 'B':
                self.count_B = self.count_B - 1
            elif letter == 'C':
                start_carrier = h.input["carrier"][0]
                end_carrier = h.input["carrier"][1]

                start_carrier_letter = ord(start_carrier[0]) - 65
                end_carrier_letter = ord(end_carrier[0]) - 65

                start_carrier_number = int(start_carrier[1:]) - 1
                end_carrier_number = int(end_carrier[1:]) - 1

                if (
                        computer_guess_number - 1 >= start_carrier_number and computer_guess_number - 1 <= end_carrier_number) and (
                        computer_guess_letter >= start_carrier_letter and computer_guess_letter <= end_carrier_letter):
                    self.count_Carrier = self.count_Carrier - 1
                else:
                    self.count_Cruiser = self.count_Cruiser - 1
            elif letter == 'S':
                self.count_S = self.count_S - 1
            elif letter == 'D':
                self.count_D = self.count_D - 1

            if self.count_B == 0 or self.count_S == 0 or self.count_D == 0 or self.count_Cruiser == 0 or self.count_Carrier == 0:
                print("You Lost!", end="")
                self.rows = 0
                self.cols = 0
                self.computer_primary_arr = []
                self.computer_tracking_arr = []
                self.computer_ship_name = []
                self.ships = []
                self.used_spaces = []
                self.count_B = 4
                self.count_Carrier = 5
                self.count_Cruiser = 3
                self.count_S = 4
                self.count_D = 2
                self.input = {}
            else:
                h.Guess()

    def print_Grid(self):
        # Primary Grid
        print("\nPrimary Grid:")
        number = 65
        for i in range(self.cols):
            print('\t', chr(number), end="")
            number = number + 1
        print()
        for i in range(self.rows):
            print(i + 1, end="")
            for j in range(self.cols):
                print('\t', self.computer_primary_arr[i][j], end="")
            print()

        #     Tracking Grid
        print("\nTracking Grid:")
        number = 65
        for i in range(self.cols):
            print('\t', chr(number), end="")
            number = number + 1
        print()
        for i in range(self.rows):
            print(i + 1, end="")
            for j in range(self.cols):
                print('\t', self.computer_tracking_arr[i][j], end="")
            print()


class Human_Move:
    rows = 0
    cols = 0
    primary_arr = []
    tracking_arr = []
    ship_name = []
    ships = []
    c = ''
    count_B = 4
    count_Carrier = 5
    count_Cruiser = 3
    count_S = 3  # submarine
    count_D = 2
    input = {}

    def quit_f(self, value):
        if value.lower() == "quit":
            print("Program terminating.\nSee summary log file for results of playing Battleship.\nThank you for playing Battleship!")
            sys.exit(0)


    def start(self):
        #TODO:input
        height_is_int = True
        length_is_int = True

        height = input("Before we begin playing, set the size of the ocean. Enter Height of Ocean Grid : ")
        while height_is_int:

            self.quit_f(height)

            try:
                height = int(height)
                height_is_int = False
            except Exception:
                print("Invalid value!")
                height = input("Before we begin playing, set the size of the ocean. Enter Height of Ocean Grid : ")

            if int(height) < 10 :

                print("Height should be greater than or equal to 10")
                # print("Length should be greater than or equal to 10")
                # print("Length should be less than 27")
                height_is_int=True
                height = input("Before we begin playing, set the size of the ocean. Enter Height of Ocean Grid : ")





        length = input("Enter Length of Ocean Grid : ")

        while length_is_int:
            self.quit_f(length)
            try:
                length = int(length)
                length_is_int = False
            except Exception:
                print("Invalid value!")
                length = input("Enter Length of Ocean Grid : ")

            if int(length) < 10 or int(length) > 27:
                # print("Height should be greater than or equal to 10")
                print("Length should be greater than or equal to 10")
                print("Length should be less than 27")
                length_is_int=True
                length = input("Enter Length of Ocean Grid : ")




        # height = int(height)
        # length = int(length)
        # if height < 10 or length < 10 or length > 27:
        #     print("Height should be greater than or equal to 10")
        #     print("Length should be greater than or equal to 10")
        #     print("Length should be less than 27")
        #     sys.exit(0)
        # else:
        self.rows, self.cols = (height, length)

        file = open("Summary_Log", 'a')
        file.write("Dimensions\n1) Height : " + str(self.rows) + "\n2) Length : " + str(self.cols))
        file.close()

        self.primary_arr = [['.' for x in range(self.cols)] for y in range(self.rows)]
        self.tracking_arr = [['.' for x in range(self.cols)] for y in range(self.rows)]
        print("******** Welcome to BattleShip Game ********")
        self.print_Grid()
        self.Place_Ship()

    def Place_Ship(self):
        self.ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        # When all ships used
        if (len(self.ship_name) == len(self.ships)):
            print("No more ships to set. Ready to play.")
            self.c = Computer_Move()
            self.c.Computer_Place_Ship()
        else:
            for i in range(len(self.ships)):
                if self.ships[i].lower() not in self.ship_name:
                    print("1", self.ships[i], "\b, ", end="")
            print('\b\b')
            # TODO:input
            ship_information = input("Place a ship of your fleet: ")
            self.quit_f(ship_information)

            if ship_information.split(" ")[0].lower() in self.ship_name:
                self.Illegal_Placement()
            #elif (len(ship_information.split(" ")) != 3):

            elif (len(ship_information.split(" ")) == 3):
                self.ship_name.append(ship_information.split(" ")[0].lower())
                ship_starting_point = ship_information.split(" ")[1].lower()
                ship_ending_point = ship_information.split(" ")[2].lower()

                # Add Ship in input dictionary
                self.input[self.ship_name[-1]] = str(ship_starting_point), str(ship_ending_point)

                self.Placement(ship_starting_point, ship_ending_point)

            else:
                print("The player must specify in this specific order:")
                print("•	the type of the ship first, (Carrier, Battleship, Cruiser, Submarine, Destroyer)")
                print("•	coordinates of the bow (the front of the ship) second")
                print("•	the coordinates of the stern (the back of the ship) last")


    def Placement(self, ship_starting_point, ship_ending_point):
        ship_start_letter = ship_starting_point[0]
        ship_end_letter = ship_ending_point[0]
        # Rows and Columns
        ship_start_number = int(ship_starting_point[1:])
        ship_end_number = int(ship_ending_point[1:])
        start_column = ord(ship_start_letter) - 96
        end_column = ord(ship_end_letter) - 96

        if self.ship_name[-1] == "carrier":
            ship_letter = "C"
            difference = 5
        elif self.ship_name[-1] == "battleship":
            ship_letter = "B"
            difference = 4
        elif self.ship_name[-1] == "cruiser":
            ship_letter = "C"
            difference = 3
        elif self.ship_name[-1] == "submarine":
            ship_letter = "S"
            difference = 3
        elif self.ship_name[-1] == "destroyer":
            ship_letter = "D"
            difference = 2
        else:
            self.Illegal_Placement()
        if (ship_end_number - ship_start_number == difference - 1) or (end_column - start_column == difference - 1):
            # Conditions
            # 1) Check whether we place ship horizontal, vertical or not
            # 2) Number we write is not outside the boundary of grid (rows)
            # 3) Letter we write is not outside the boundary of grid (cols)

            if ((ship_start_number == ship_end_number) or (ship_start_letter == ship_end_letter)) and (
                    (ship_start_number <= self.rows) and (ship_end_number <= self.rows)) and (
                    (start_column <= self.cols) and (end_column <= self.cols)):
                for i in range(ship_start_number - 1, ship_end_number):
                    for j in range(start_column - 1, end_column):
                        if self.primary_arr[i][j] == ".":
                            self.primary_arr[i][j] = ship_letter
                        else:
                            self.ship_name.pop()
                            self.Illegal_Placement()
                self.Place_Ship()
            else:
                self.ship_name.pop()
                self.Illegal_Placement()
        else:
            self.ship_name.pop()
            self.Illegal_Placement()

    def Illegal_Placement(self):
        print("Illegal Placement")
        self.Place_Ship()

    def play(self):
        self.tracking_arr = [['?' for x in range(self.cols)] for y in range(self.rows)]
        self.print_Grid()
        self.Guess()

    def Guess(self):
        # TODO:input
        guess = input("Guess Target Space : ").lower()
        self.quit_f(guess)
        file = open("Summary_Log", 'a')
        file.write("\nHuman Guess : " + guess)
        file.close()

        human_guess_letter = ord(guess[0]) - 96
        human_guess_number = int(guess[1:])

        # -1 because rows and columns starts from 0
        if self.c.computer_primary_arr[human_guess_number - 1][human_guess_letter - 1] == ".":
            print("Miss!")
            self.tracking_arr[human_guess_number - 1][human_guess_letter - 1] = "M"
            self.c.Computer_Guess()
        else:
            print("Hit!")
            self.tracking_arr[human_guess_number - 1][human_guess_letter - 1] = "X"
            letter = self.c.computer_primary_arr[human_guess_number - 1][human_guess_letter - 1]

            if letter == 'B':
                self.count_B = self.count_B - 1
            elif letter == 'C':

                start_carrier = self.c.input["carrier"][0]
                end_carrier = self.c.input["carrier"][1]

                start_carrier_letter = ord(start_carrier[0]) - 65
                end_carrier_letter = ord(end_carrier[0]) - 65

                start_carrier_number = int(start_carrier[1:])
                end_carrier_number = int(end_carrier[1:])
                # fix this part double print (this is fixed)

                if (
                        human_guess_number - 1 >= start_carrier_number and human_guess_number - 1 <= end_carrier_number) and (
                        human_guess_letter - 1 >= start_carrier_letter and human_guess_letter - 1 <= end_carrier_letter):
                    self.count_Carrier = self.count_Carrier - 1
                else:
                    self.count_Cruiser = self.count_Cruiser - 1
            elif letter == 'S':
                self.count_S = self.count_S - 1
            elif letter == 'D':
                self.count_D = self.count_D - 1
            if self.count_B == 0 or self.count_S == 0 or self.count_D == 0 or self.count_Cruiser == 0 or self.count_Carrier == 0:
                print("You Won!", end="")
                self.rows = 0
                self.cols = 0
                self.primary_arr = []
                self.tracking_arr = []
                self.ship_name = []
                self.ships = []
                self.c = ''
                self.count_B = 4
                self.count_Carrier = 5
                self.count_Cruiser = 3
                self.count_S = 4
                self.count_D = 2
                self.input = {}
            else:
                self.c.Computer_Guess()

    def print_Grid(self):
        # Primary Grid
        print("\nPrimary Grid:")
        number = 65
        for i in range(self.cols):
            print('\t', chr(number), end="")
            number = number + 1
        print()
        for i in range(self.rows):
            print(i + 1, end="")
            for j in range(self.cols):
                print('\t', self.primary_arr[i][j], end="")
            print()

        #     Tracking Grid
        print("\nTracking Grid:")
        number = 65
        for i in range(self.cols):
            print('\t', chr(number), end="")
            number = number + 1
        print()
        for i in range(self.rows):
            print(i + 1, end="")
            for j in range(self.cols):
                print('\t', self.tracking_arr[i][j], end="")
            print()


if __name__ == '__main__':
    h = Human_Move()
    h.start()
    # TODO:input
    again = input("Let's play again? > ")
    h.quit_f(again)
    while again.lower() == "yes":
        h = Human_Move()
        h.start()

